window.onload = function(){


function runPyScript(message){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/trifid",
        async: false,
        data: { 'message2encrypt': message2encrypt},
        success: function(result) {
          // console.log(result);
          document.getElementById('encryptedbox').innerHTML = result['encrypted'];
        },
        error: function() {
          document.getElementById('decryptedbox').innerHTML = 'Error'
          // alert("FAIL");
        },
    });

    return jqXHR.responseText;
}

function runDecryptor(message){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/trifid",
        async: false,
        data: { 'message2decrypt': message2decrypt},
        success: function(result) {
          // console.log(result);
          document.getElementById('decryptedbox').innerHTML = result['decrypted'];
        },
        error: function() {
          document.getElementById('decryptedbox').innerHTML = 'Error'
          // alert("FAIL");
        },
    });

    return jqXHR.responseText;
}






var encryptbox = document.getElementById('encryptbox');
var decryptbox = document.getElementById('decryptbox');



encryptbox.onkeyup = function(){
    message2encrypt = encryptbox.value;
    runPyScript(message2encrypt);
}



decryptbox.onkeyup = function(){
    message2decrypt = decryptbox.value;
    runDecryptor(message2decrypt);
}


// This transitions from the print stuff above to the copy stuff below.
var encryptCopyBtn = document.querySelector('#encryptcopy');

encryptCopyBtn.addEventListener('click', function(event) {
	var encryptedText = document.querySelector('#encryptedbox');
  encryptedText.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
	  } catch (err) {
	  console.log('Oops, unable to copy');
  }
});



var decryptCopyBtn = document.querySelector('#decryptcopy');

decryptCopyBtn.addEventListener('click', function(event) {
	var decryptedText = document.querySelector('#decryptedbox');
  decryptedText.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
	  } catch (err) {
	  console.log('Oops, unable to copy');
  }
});





}
