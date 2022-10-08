import sys
num = eval(input("section number:(11,22,33,44) "))
startnum = eval(input("page start:"))
endnum = eval(input("page end:"))
content = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>Document</title>
    <link rel="stylesheet" href="../../bootstrap-4.6.1-dist/css/bootstrap.css" />
    <link rel="stylesheet" href="../../model/highlight/styles/atom-one-light.min.css" />
    <link rel="stylesheet" href="../../css/article.css" />
    <link rel="stylesheet" href="../../css/animate.css" />
    <script type="text/javascript" src="../../js/jquery-3.5.1.js"></script>
    <script type="text/javascript" src="../../model/highlight/highlight.js"></script>
    <script type="text/javascript" src="../../model/highlight/languages/xml.min.js"></script>
    <script type="text/javascript" src="../../model/highlight/languages/css.min.js"></script>
    <script type="text/javascript" src="../../model/js/clipboard.min.js"></script>
    <script type="text/javascript" src="../../model/js/code.js"></script>
</head>

<body>
<div id="mask">
        <svg t="1642696614079" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
            p-id="2129" width="200" height="200">
            <path
                d="M85.333333 512C85.333333 276.352 276.309333 85.333333 512 85.333333c235.648 0 426.666667 190.976 426.666667 426.666667 0 235.648-190.976 426.666667-426.666667 426.666667-235.648 0-426.666667-190.976-426.666667-426.666667z m426.666667-30.165333l-105.685333-105.706667a21.269333 21.269333 0 0 0-30.08 0.106667 21.205333 21.205333 0 0 0-0.106667 30.08L481.834667 512l-105.706667 105.685333a21.269333 21.269333 0 0 0 0.106667 30.08 21.205333 21.205333 0 0 0 30.08 0.106667L512 542.165333l105.685333 105.706667a21.269333 21.269333 0 0 0 30.08-0.106667 21.205333 21.205333 0 0 0 0.106667-30.08L542.165333 512l105.706667-105.685333a21.269333 21.269333 0 0 0-0.106667-30.08 21.205333 21.205333 0 0 0-30.08-0.106667L512 481.834667z"
                p-id="2130"></path>
        </svg>
        <img src="" alt="" id="maskimg">
    </div>
    <div id="CopySuccessInfo">
        <div class="col-md-2 offset-5">
            <div class="text-success text-center" id="success">Success!</div>
        </div>
    </div>
     <div id="CopyErrorInfo">
        <div class="col-md-2 offset-5">
            <div class="text-danger text-center" id="error">Error!</div>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-md-12"></div>
        </div>
    </div>
</body>

</html>
"""
for i in range(startnum, endnum+1):
    file = open("D:\\github-progect\\class\\section\\section"+str(num)+"\\" +
                str(i)+".html", "w")
    file.write(content)
    file.close()
