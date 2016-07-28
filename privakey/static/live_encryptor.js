window.onload = function(){


function runPyScript(message, code_word){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/cycle",
        async: false,
        data: { 'message2encrypt': message2encrypt, 'code_word': code_word },
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

function runDecryptor(message, code_word){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/cycle",
        async: false,
        data: { 'message2decrypt': message2decrypt, 'code_word': code_word },
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
var code_word = document.getElementById('code_word');



encryptbox.onkeyup = function(){
    message2encrypt = encryptbox.value;
    runPyScript(message2encrypt,code_word.value);
}



decryptbox.onkeyup = function(){
    message2decrypt = decryptbox.value;
    runDecryptor(message2decrypt,code_word.value);
}



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
