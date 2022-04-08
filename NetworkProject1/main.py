from socket import *

# set the port to 9000.
serverPort = 9000
# creating the socket and initialize it.
serverSocket = socket(AF_INET, SOCK_STREAM)
# defines a relationship between the socket and theIP address that are available on the host.
serverSocket.bind(("0.0.0.0", serverPort))  # 192.168.1.158 is the IP address version 4 of my PC
# opens the bound port so the socket can then start receiving connections from clients.
serverSocket.listen(1)
# print a work done message.
print("The server is ready to receive")
PhoneNum = {}

while True:  # loop forever
    # server waits on accept() for incoming requests, new socket created on return
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]  # get the ip address and save it in ip variable
    port = addr[1]  # get the port number and save it in port variable
    # read bytes from socket (but not address as in UDP)
    sentence = connectionSocket.recv(
        1024).decode()
    data = sentence.split(" ")
    print(data[1])
    print(addr)
    # print the IP and port number of the client on command line window.
    print(sentence)
    # send the web style by the response.
    if data[1] == "/index.html" or data[1] == "/":
        # sending 200 OK response
        connectionSocket.send((
            "HTTP/1.1 200 OK\r\n".encode()))
        connectionSocket.send(
            "Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = """ 
        <!DOCTYPE html>
<html lang = "en"> 
<head>
  <Title>ENCS3320 Simple Webserver</Title> 
  <meta charset="utf-8">

</head>
<style> html,
body {
  height: 100%;
}
 .center{
      text-align: center;
    color: white;
    font-family: Times New Roman;
    font-size: 20px;
    }
     .images{
text-align: center;
 margin-top: 266px;
  margin-bottom: 700px;

    }

     .Names{
      text-align: center;
    color: white;
    font-family: Courier New;
    font-weight: bold;
    font-size: 20px;
    }
body {
  margin: 0;
  background: linear-gradient(45deg, #49a09d, #5f2c82);
  font-family: sans-serif;
  font-weight: 100;
}

.container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

table {
  display: block;
  width: 900px;
  border-collapse: collapse;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0,0,0,0.1);
}

th,
td {
  padding: 15px;
  background-color: rgba(255,255,255,0.2);
  color: #fff;
}

th {
  text-align: center;
}

thead {
  th {
    background-color: #55608f;
  }
}
 .color{
       color: #7BCCB5; 
    }
tbody {
  tr {
    &:hover {
      background-color: rgba(255,255,255,0.3);
    }
  }
  td {
    position: relative;
    &:hover {
      &:before {
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        top: -9999px;
        bottom: -9999px;
        background-color: rgba(255,255,255,0.2);
        z-index: -1;
      }
    }
  }
}
</style>
<body>
  <div class="center">
  <H1>Welcome to our course 

<span class="color" >Computer Networks</span>
</H1> 
</div>
<HR>
<p>
<div class="Names">Yasmin Jwabreh - 1180815 <BR> 
Nour Malaki - 1181275 <BR> 
Haleema Hmedan - 1172743 <BR> </div>

</p>
<HR>

<div class="container">
  <table>
    <thead>
      <tr>
        <th>Yasmin Jwabreh</th>
        <th>Nour Malaki</th>
        <th>Haleema Hmedan</th>
      </tr>
    </thead>
    <tbody>
      <tr>
       <td> In this semester, I'm Working on Artificial Intelligence Project; Optimal service and Machine learning, Integrated Circuit project, Network Project; Web Server with html and css. I have coding skills, problem solving. </td>
    <td> In this semester, I'm Working on Managment engineering project, also, Artificial Intelligence projects about Optimal service and Machine learning, Network Project; Web Server with html and css. I have coding skills, problem solving. </td>
    <td> In this semester, I'm Working on Interfacing Techniques Project,Artificial Intelligence Project; Optimal service and Machine learning, Real Time and Embedded System projects, Network Project; Web Server with html and css,Android Studio and manegment Project  . I have coding skills, problem solving. </td>
      </tr>
    </tbody>
  </table>
</div>
<div class="images"><img src="NetworkProject.jpg" alt="NetworkProjectJPG" width="400" height="333"  vspace="20" hspace="20">
<img src="NetworkProject.png" alt="NetworkProjectPNG" width="400" height="333" vspace="20" hspace="20">
<br>
</div>
</body>
</html>

"""
        connectionSocket.send(s.encode())  # send html text to clinet
        connectionSocket.close()

    elif (data[1].endswith('NetworkProject.png') or data[1].endswith('NetworkProject.png/')):

        name = data[1].split('/')[1]
        type = data[1].split('.')[1]
        # sending 200 OK response

        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send(("Content-Type: image/" + type + "\r\n").encode())
        connectionSocket.send("\r\n".encode())
        # path = os.path.join('net5'+name)
        image_os = open(name, 'rb')
        imageInfo = image_os.read()
        image_os.close()
        connectionSocket.send(imageInfo)
        connectionSocket.close()

    elif (data[1].endswith('NetworkProject.jpg') or data[1].endswith('NetworkProject.jpg/')):
        name = data[1].split('/')[1]
        type = data[1].split('.')[1]
        # sending 200 OK response

        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send(("Content-Type: image/" + type + "\r\n").encode())
        connectionSocket.send("\r\n".encode())
        image_os = open(name, 'rb')
        imageInfo = image_os.read()
        image_os.close()
        connectionSocket.send(imageInfo)
        connectionSocket.close()

    elif data[1].startswith("/Sort"):
        # sending the request response
        connectionSocket.send((
            "HTTP/1.1 200 OK\r\n".encode()))
        str = []
        thisDict = {}
        # open data file
        with open("smartphones.txt", "r") as my_file:
            # spliting the data by comma ","
            my_file = my_file.read().splitlines()
            for line in my_file:
                str.append(line.split(","))
        for k in range(len(str)):
            for j in range(len(str[k]) - 1):
                # thisDict dictionary contains the smart phone with there prices
                thisDict[str[k][j]] = int(str[k][j + 1])
        # checking the request to sort
        if (data[1].endswith("Name")):
            sorted_names = sorted(thisDict.items())
            array = []
            # sending the html file with sorted names
            connectionSocket.send(
                "Content-Type: text/html \r\n".encode())
            connectionSocket.send("\r\n".encode())
            s = """
          <!DOCTYPE html>
<html lang="en">
<head>
	<title>
		Smart Phones Price Sorted
	</title>
	<style>
html,
body {
  height: 100%;
}
body {
  margin: 0;
  background: -webkit-linear-gradient(45deg, #49a09d, #5f2c82);
  background: linear-gradient(45deg, #49a09d, #5f2c82);
  font-family: sans-serif;
  font-weight: 100;
}
.container {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
}
table {
  width: 800px;
  border-collapse: collapse;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
th,
td {
  padding: 15px;
  background-color: rgba(255, 255, 255, 0.2);
  color: #fff;
}
th {
  text-align: left;
}
thead th {
  background-color: #55608f;
}
tbody tr:hover {
  background-color: rgba(255, 255, 255, 0.3);
}
tbody td {
  position: relative;
}
tbody td:hover:before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -9999px;
  bottom: -9999px;
  background-color: rgba(255, 255, 255, 0.2);
  z-index: -1;
}

.Names{
   text-align: center;
    color: white;
    font-family: Courier New;
    font-weight: bold;
    font-size: 20px;
}
</style>
</head>

<body>
  <div class="Names"><H1 ALIGN="CENTER"> Smart Phones with Prices Sample </H1> </div>


<HR>

<div class="container">
  <table>
    <tr>
    <th>Phone Name</th>
    <th>Phone Price </th>
  </tr>
  <tr>
    <td> """ + sorted_names[0][0] + f"""</td>
    <td> {sorted_names[0][1]} </td>
  </tr>
  <tr>
    <td> """ + sorted_names[1][0] + f"""</td>
    <td>{sorted_names[1][1]}</td>
  </tr>
  <tr>

    <td>""" + sorted_names[2][0] + f"""</td>
    <td>{sorted_names[2][1]}</td>
  </tr>
  <tr>
    <td> """ + sorted_names[3][0] + f""" </td>
    <td>{sorted_names[3][1]}</td>
  </tr>
<tr>
    <td> """ + sorted_names[4][0] + f"""
</td>
    <td>{sorted_names[4][1]}</td>
  </tr>
  </table>
</div>
</body>
</html>"""  # html text that show simple web page
            connectionSocket.send(s.encode())  # send html text to clinet
            connectionSocket.close()

        if (data[1].endswith("Price")):
            sorted_prices = {}
            Sorted = sorted(thisDict, key=thisDict.get)
            for w in Sorted:
                sorted_prices[w] = thisDict[w]
            # sending the html file with sorted prices

            connectionSocket.send(
                "Content-Type: text/html \r\n".encode())
            connectionSocket.send("\r\n".encode())
            s = """
                          <!DOCTYPE html>
<html lang="en">
<head>
	<title>
		Smart Phones Price Sorted
	</title>
	<style>
html,
body {
  height: 100%;
}
body {
  margin: 0;
  background: -webkit-linear-gradient(45deg, #49a09d, #5f2c82);
  background: linear-gradient(45deg, #49a09d, #5f2c82);
  font-family: sans-serif;
  font-weight: 100;
}
.container {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
}
table {
  width: 800px;
  border-collapse: collapse;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
th,
td {
  padding: 15px;
  background-color: rgba(255, 255, 255, 0.2);
  color: #fff;
}
th {
  text-align: left;
}
thead th {
  background-color: #55608f;
}
tbody tr:hover {
  background-color: rgba(255, 255, 255, 0.3);
}
tbody td {
  position: relative;
}
tbody td:hover:before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -9999px;
  bottom: -9999px;
  background-color: rgba(255, 255, 255, 0.2);
  z-index: -1;
}

.Names{
   text-align: center;
    color: white;
    font-family: Courier New;
    font-weight: bold;
    font-size: 20px;
}
</style>
</head>

<body>
  <div class="Names"><H1 ALIGN="CENTER"> Smart Phones with Prices Sample </H1> </div>


<HR>

<div class="container">
  <table>
    <tr>
                <th>Phone Name</th>
                <th>Phone Price </th>
              </tr>
              <tr>
                <td> """ + list(sorted_prices.keys())[0] + f"""</td>
                <td> {list(sorted_prices.values())[0]} </td>
              </tr>
              <tr>
                <td> """ + list(sorted_prices.keys())[1] + f"""</td>
                <td>{list(sorted_prices.values())[1]}</td>
              </tr>
              <tr>

                <td>""" + list(sorted_prices.keys())[2] + f"""</td>
                <td>{list(sorted_prices.values())[2]}</td>
              </tr>
              <tr>
                <td> """ + list(sorted_prices.keys())[3] + f""" </td>
                <td>{list(sorted_prices.values())[3]}</td>
              </tr>
            <tr>
                <td> """ + list(sorted_prices.keys())[4] + f"""
            </td>
                <td>{list(sorted_prices.values())[4]}</td>
              </tr>
  </table>
</div>
</body>
</html> """  # html text that show simple web page

            connectionSocket.send(s.encode())  # send html text to clinet
            connectionSocket.close()

    else:
        # sending 404 respnse status
        connectionSocket.send(
            "HTTP/1.1 404 Not found\r\n".encode())
        connectionSocket.send(
            "Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        # sending the html error file to open
        s = """ <!DOCTYPE html>
<html lang="en">
<head>
	<title>
		ERROR
	</title>
</head>
<style >


body {
  padding: 0;
  margin: 0;
}

#notfound {
  position: relative;
  height: 100vh;
  background-color: #222;
}

#notfound .notfound {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
      -ms-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
}

.notfound {
  max-width: 460px;
  width: 100%;
  text-align: center;
  line-height: 1.4;
}

.notfound .notfound-404 {
  height: 158px;
  line-height: 153px;
}

.notfound .notfound-404 h1 {
  font-family: 'Josefin Sans', sans-serif;
  color: #222;
  font-size: 220px;
  letter-spacing: 10px;
  margin: 0px;
  font-weight: 700;
  text-shadow: 2px 2px 0px #c9c9c9, -2px -2px 0px #c9c9c9;
}

.notfound .notfound-404 h1>span {
  text-shadow: 2px 2px 0px #ffab00, -2px -2px 0px #ffab00, 0px 0px 8px #ff8700;
}

.notfound p {
  font-family: 'Josefin Sans', sans-serif;
  color: #c9c9c9;
  font-size: 16px;
  font-weight: 400;
  margin-top: 0px;
  margin-bottom: 15px;
}



@media only screen and (max-width: 480px) {
  .notfound .notfound-404 {
    height: 122px;
    line-height: 122px;
  }

  .notfound .notfound-404 h1 {
      font-size: 122px;
  }
}

.Names{
	 text-align: center;
    color: white;
    font-family: Courier New;
    font-weight: bold;
    font-size: 20px;
}
</style>
<body>
<div id="notfound">
	<p>
		<div class="Names">
			<br>
			Yasmin Jwabreh - 1180815 <BR> 
            Nour Malaki - 1181275 <BR> 
            Haleema Hmedan - 1172743 <BR> 

            <hr>
		</div>
    </p>
    """ + f"""
		<div class="notfound">
			<div class="notfound-404">
				<h1>4<span>0</span>4</h1>
			</div>
			<p><br> Not Found! The page you are looking for might have been removed had its name changed or is temporarily unavailable.
				<br><br>
			   IP Address: {ip}
	           <br><br>
	           Port Number: {port}
            </p>

		</div>
	</BR>
</BR>
	</div>
</body>
</html>"""
        connectionSocket.send(s.encode())
        connectionSocket.close()
