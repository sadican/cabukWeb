class BasicTemplate:
  'Basic template for html page'
  
  def __init__(self):
    print 'hobarey!'
  
  def getHeader(self, title):
    return '<!DOCTYPE html>'
      + "\n" + '<html lang="en">' +
      + "\n" + '<head>' +
      + "\n" + '<meta charset="utf-8">' +
      + "\n" + '<meta http-equiv="X-UA-Compatible" content="IE=edge">' +
      + "\n" + '<meta name="viewport" content="width=device-width, initial-scale=1">' +
      + "\n" + '<title>' + title + '</title>' +
      + "\n" + '<!-- Bootstrap -->' +
      + "\n" + '<link href="css/bootstrap.min.css" rel="stylesheet">' +
      + "\n" + '<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->' +
      + "\n" + '<!-- WARNING: Respond.js doesnt work if you view the page via file:// -->' +
      + "\n" + '<!--[if lt IE 9]>' +
      + "\n" + '<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>' +
      + "\n" + '<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>' +
      + "\n" + '<![endif]-->' +
      + "\n" + '</head>' +
      + "\n" + '<body>'
  
  def getFooter(self):
    return '<!-- jQuery (necessary for Bootstraps JavaScript plugins) -->'
      + "\n" + '<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>' +
      + "\n" + '<!-- Include all compiled plugins (below), or include individual files as needed -->' +
      + "\n" + '<script src="js/bootstrap.min.js"></script>' +
      + "\n" + '</body>' +
      + "\n" + '</html>"'
