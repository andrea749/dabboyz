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
          alert("FAIL");
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
          alert("FAIL");
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


}
