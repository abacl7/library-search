#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import urllib
import json

api_url = "http://api.calil.jp/library?"

# API Key
# API Spec: https://calil.jp/doc/api_ref.html
apikey = "YOUR_API_KEY"

# get Form param
form = cgi.FieldStorage()

# make query param
if form.has_key('pref'):
    pref = form['pref'].value
else:
    pref = ''

if form.has_key('city'):
    city = form['city'].value
else:
    city = ''

param = urllib.urlencode(
               {'appkey': apikey,
                'format': "json",
                'callback': "",
                'pref': pref,
                'city': city,
               })
queryString = api_url + param

# API call exec
response = urllib.urlopen(queryString)

# make json from api call result
json_obj = json.loads(response.read(), 'utf-8')

# make response html
print "Content-type: text/html\n"
print """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Search Library Result</title>
  </head>
  <body>
    <hr>
    <table border="1">
    <tr>
      <th>郵便番号</th>
      <th>住所</th>
      <th>略称</th>
      <th>正式名称</th>
      <th>電話番号</th>
    </tr>
"""

for data in json_obj:
    systemid = data['systemid']
    systemid = eval("u'''%s'''" % systemid).encode('utf-8')
    libkey = data['libkey']
    libkey = eval("u'''%s'''" % libkey).encode('utf-8')
    post = data['post']
    post = eval("u'''%s'''" % post).encode('utf-8')
    address = data['address']
    address = eval("u'''%s'''" % address).encode('utf-8')
    short_name = data['short']
    short_name = eval("u'''%s'''" % short_name).encode('utf-8')
    formal_name = data['formal']
    formal_name = eval("u'''%s'''" % formal_name).encode('utf-8')
    tel = data['tel']
    tel = eval("u'''%s'''" % tel).encode('utf-8')
    link_url = "http://calil.jp/library/search?s=" + systemid + "&k=" + libkey

    print "    <tr>"
    print "      <td>"
    print post
    print "      </td>"
    print "      <td>"
    print address
    print "      </td>"
    print "      <td>"
    print short_name
    print "      </td>"
    print "      <td>"
    print """
          <a href="
    """
    print link_url
    print """
          ">
    """
    print formal_name
    print "      </a>"
    print "      </td>"
    print "      <td>"
    print tel
    print "      </td>"
    print "      <td>"
    print "    </tr>"
print """
    </table>
    <hr>
    <div align="right">
    <a href="../index.html">戻る</a>
    </div>
  </body>
</html>
"""
