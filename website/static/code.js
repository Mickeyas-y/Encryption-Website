
  function encrypt() {

   var algorithm = $('#encalgorithm').find('option:selected').text();
   var plaintext = $('#enctextbox').val();
   var secret = $('#encsecret').val();

   var mode = $('#encoption').find('option:selected').text();
   var pad = $('#encpadoption').find('option:selected').text();

        var key = CryptoJS.enc.Base64.parse('fly12345678alltheplanetfivetimes');
        var iv = CryptoJS.enc.Base64.parse('doesnotmeanindividualvaluebutgardens7890102345blueworld');

   var encMode;
   var encPadding;

   if (mode == "CBC") {
        encMode = "mode: CryptoJS.mode.CBC";
   } else if (mode == "CFB") {
        encMode = "mode: CryptoJS.mode.CFB";
   } else if (mode == "CTR") {
        encMode = "mode: CryptoJS.mode.CTR";
   } else if (mode == "ECB") {
        encMode = "mode: CryptoJS.mode.ECB";
   } else if (mode == "OFB") {
        encMode = "mode: CryptoJS.mode.OFB";
   }

   if (pad == "Pkcs7") {
        encPadding = "padding: CryptoJS.pad.Pkcs7";
   } else if (pad == "AnsiX923") {
        encPadding = "padding: CryptoJS.pad.AnsiX923";
   } else if (pad == "Iso97971") {
        encPadding = "padding: CryptoJS.pad.Iso97971";
   } else if (pad == "Iso10126") {
        encPadding = "padding: CryptoJS.pad.Iso10126";
   } else if (pad == "NoPadding") {
        encPadding = "padding: CryptoJS.pad.NoPadding";
   } else if (pad == "ZeroPadding") {
        encPadding = "padding: CryptoJS.pad.ZeroPadding";
   }

   if (algorithm == "AES") {
       var encrypted = CryptoJS.AES.encrypt(plaintext, secret, key, {iv: iv, encMode, encPadding});
   } else if (algorithm == "3DES") {
       var encrypted = CryptoJS.TripleDES.encrypt(plaintext, secret, key, {iv: iv, encMode, encPadding});
   } else if (algorithm == "DES") {
       var encrypted = CryptoJS.DES.encrypt(plaintext, secret, key, {iv: iv, encMode, encPadding});
   } else if (algorithm == "RABBIT") {
       var encrypted = CryptoJS.Rabbit.encrypt(plaintext, secret, key, {iv: iv, encMode, encPadding});
   } else if (algorithm == "RC4") {
       var encrypted = CryptoJS.RC4.encrypt(plaintext, secret, key, {iv: iv, encMode, encPadding});
   } else if (algorithm == "HmacSHA512") {
        var encrypted = CryptoJS.HmacSHA512(plaintext, secret, key, {iv: iv, encMode, encPadding});
   } else if (algorithm == "SHA512") {
        var encrypted = CryptoJS.SHA512(plaintext, secret, key, {iv: iv, encMode, encPadding});
   } else if (algorithm == "HmacMD5") {
        var encrypted = CryptoJS.HmacMD5(plaintext, secret, key, {iv: iv, encMode, encPadding});
   }

    var d = new Date();

   $("#id_encrypted_message").attr('disabled', false);

   $("#id_encrypted_message").val( "" + encrypted );

   $("#id_encrypted_message").attr('disabled', true);

   $("#encoutput").html(" <ul> Encrypted successfully " + " <br>" + "Original text: <br>" + "<p>" + plaintext + "</p>" + " Please store your passphrase safely </ul>" );


   return false;

  };