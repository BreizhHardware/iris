function checkFeatures() {
    nbFeatures = 0
    if (document.forms["features"]["sepal-length"].value != '') {
      nbFeatures = nbFeatures + 1 ;
    }
    if (document.forms["features"]["sepal-width"].value != '') {
      nbFeatures = nbFeatures + 1 ;
    }
    if (document.forms["features"]["petal-length"].value != '') {
      nbFeatures = nbFeatures + 1 ;
    }
    if (document.forms["features"]["petal-width"].value != '') {
      nbFeatures = nbFeatures + 1 ;
    }
    if (nbFeatures < 2) {
      alert("Waring: You need to put at least 2 characteristics.");
      return false ;
    }
  }