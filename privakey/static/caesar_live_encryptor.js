window.onload = function(){


function runPyScript(message, shift){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/caesar",
        async: false,
        data: { 'message2encrypt': message2encrypt, 'shift': shift },
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

function runDecryptor(message, shift){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/caesar",
        async: false,
        data: { 'message2decrypt': message2decrypt, 'shift': shift },
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
var shift = document.getElementById('shift');



encryptbox.onkeyup = function(){
    message2encrypt = encryptbox.value;
    runPyScript(message2encrypt,shift.value);
}



decryptbox.onkeyup = function(){
    message2decrypt = decryptbox.value;
    runDecryptor(message2decrypt,shift.value);
}


}
