import re
import json
import ast
import http.client

def fetch_html(url):
    conn = http.client.HTTPSConnection("tak-wls-prod.wahlap.net")
    conn.request("GET", url)
    res = conn.getresponse()
    return res.read().decode("utf-8")

def extract_js_path(html):
    match = re.search(r'app\.[\w\d]+\.js', html)
    return match.group(0) if match else None

def fetch_js(js_path):
    conn = http.client.HTTPSConnection("tak-wls-prod.wahlap.net")
    conn.request("GET", f"/file/dist/js/{js_path}")
    res = conn.getresponse()
    return res.read().decode("utf-8")

def extract_song_data(js):
    matches = re.findall(r'JSON\.parse\((.*?)\)\}', js)
    return [match for match in matches if 'song_name_jp' in match]

def main():
    html = fetch_html("/file/dist/")
    js_path = extract_js_path(html)

    if js_path:
        js = fetch_js(js_path)
        results = extract_song_data(js)

        if results:
            taiko_songs = json.loads(ast.literal_eval(results[0]))
            json_str = json.dumps(taiko_songs, indent=4, ensure_ascii=False)
            print(json_str)
        else:
            print("No song data found.")
    else:
        print("JavaScript path not found.")

if __name__ == "__main__":
    main()
