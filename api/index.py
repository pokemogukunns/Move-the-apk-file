from flask import Flask, request, jsonify
import apkutils

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "APK Runner is running!"

@app.route("/upload", methods=["POST"])
def upload_apk():
    if "apk" not in request.files:
        return jsonify({"error": "No APK file uploaded"}), 400

    apk_file = request.files["apk"]
    parser = apkutils.APK(apk_file.stream.read())
    
    return jsonify({
        "package": parser.package_name,
        "version": parser.version_name,
        "permissions": list(parser.get_permissions())
    })

if __name__ == "__main__":
    app.run()
