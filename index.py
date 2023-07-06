from flask import Flask,request
import openai,base64

app=Flask(__name__)
openaikey="c2stOGtlYW9FQk1qRWZQRnJzQ0tlNlRUM0JsYmtGSllSWk9wMkN3Mk9VSFhMNjZZNEZY";
openaikey=openaikey.encode('ascii')
openaikey=base64.b64decode(openaikey).decode('ascii')
openai.api_key=openaikey

@app.route("/gen-image",methods=["GET"])
def create_image()->str:
    data=request.args.get("data")
    print(data)
    prompt=f"Generate professional image for {data}"
    response=openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    return response["data"][0]["url"]
    
if __name__=="__main__":
    app.run(5000,debug=False)