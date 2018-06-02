from urllib import request

goog_url = "http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv"


def download_file(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'csvdown.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_file(goog_url)

