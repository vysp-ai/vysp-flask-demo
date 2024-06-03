import os
from openai import OpenAI
from flask import Flask, redirect, render_template, request, url_for
from vysp import VYSPClient
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



client = VYSPClient(tenant_api_key=os.getenv("VYSP_TENANT_API_KEY"),
                    gate_api_key=os.getenv("VYSP_GATE_API_KEY"),
                    installation_type="cloud")

openai_client = OpenAI()


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        check_input_result = client.check_input(client_ref_user_id="user_id",
                                  client_ref_internal=False,
                                  prompt=question,
                                  metadata={"client_info": "client_information"})
        print("Input Result: ", check_input_result)
        if check_input_result["flagged"]:
            error = "Please adjust your input prompt. Your input was flagged as a possible high-risk input."
            return redirect(url_for("index", error=error))
        
        response = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-3.5-turbo",
        )
        check_output_result = client.check_output(client_ref_user_id="user_id",
                                  client_ref_internal=False,
                                  prompt=question,
                                  model_output=response.choices[0].message.content,
                                  metadata={"client_info": "client_information"})
        print("Output Result: ", check_output_result)
        if check_output_result["flagged"]:
            error = " Sorry, there was an error with the model output."
            return redirect(url_for("index", error=error))
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    error = request.args.get("error")
    return render_template("index.html", result=result, error=error)

@app.route("/insecure", methods=("GET", "POST"))
def insecure():
    if request.method == "POST":
        question = request.form["question"]


        response = openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return redirect(url_for("insecure", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("insecure.html", result=result)

