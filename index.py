from flask import Flask,request
import openai,base64,json
from flask_cors import CORS,cross_origin

app=Flask(__name__)
CORS(app)
openaikey="c2stY2U3dFlvQkVkaE44czNrendIRzlUM0JsYmtGSjFMYTBhTFN4cDg3NndCRDlRa1RT";
openaikey=openaikey.encode('ascii')
openaikey=base64.b64decode(openaikey).decode('ascii')
openai.api_key=openaikey
app.config['CORS_HEADERS'] = 'Content-Type'

def sum_text(text)->str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize this for a second-grade student removing any proper nouns:\n\n{text}",
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.get('choices')[0].get('text').strip()

@app.route("/gen-image",methods=["GET"])
@cross_origin()
def create_image()->str:
    data=request.args.get("data")
    print(data)
    print(sum_text(data))
    prompt=f"A  photo without any text in it describing : \n\n{sum_text(data)}"
    response=openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    return {"data":response["data"][0]["url"],"id":request.args.get("id")}
    #response.get('choices')[0].get('text').strip()
if __name__=="__main__":
    app.run(5000,debug=False)