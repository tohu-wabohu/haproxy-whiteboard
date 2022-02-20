from flask import Flask, render_template, request, flash
import json
import ipaddress
import pprint

app = Flask(__name__)
app.secret_key = b'vJ6mDThaTyanFHxiLKX7'    # This is not safe. Don't do like this on production

@app.route("/", methods = ['GET','POST'])
def main():
    with open('ips.json') as json_file:
        data = json.load(json_file)

    if request.method == 'POST':
        if "ip" in request.form:
            ip = request.form['ip']
            comment = request.form['comment']
            #-- sanity check -------------------------------------
            if ip == "":
                flash("N/A", "no_ip")
                return render_template('index.html', items=data)
            if comment == "":
                flash("N/A", "no_comment")
                return render_template('index.html', items=data)
            try:
                ip_not_used = ipaddress.ip_address(ip)
                pass
            except ValueError:
                flash(ip, "bad_ip")
                return render_template('index.html', items=data)
            #-----------------------------------------------------
            data[ip] = comment
            with open('ips.json', 'w') as json_file:
                json.dump(data, json_file)
            with open('ips.txt', 'w') as txt_file:
                for k in data:
                    txt_file.write(k + "/32\n")
                
        elif "remove" in request.form:
            key = request.form['key']
            del data[key]
            with open('ips.json', 'w') as json_file:
                json.dump(data, json_file)
            with open('ips.txt', 'w') as txt_file:
                for k in data:
                    txt_file.write(k + "/32\n")

    with open('ips.json') as json_file:
        json_object = json.load(json_file)
        print(type(json_object))
        ips_json = json.dumps(json_object, indent=4)
    with open('ips.txt') as txt_file:
        ips_txt = txt_file.read()
    return render_template('index.html', items=data, ips_json=ips_json, ips_txt=ips_txt)


# Do not run Flask server on production. This has a debug mode on which makes server extra unsafe!!!
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 

