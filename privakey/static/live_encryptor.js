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


}
