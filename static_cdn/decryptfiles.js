    function decryptfile() {
        var file = document.getElementById("in_file").files[0];
        var password = $('#id_password').val();

        var key = CryptoJS.enc.Base64.parse('fly12345678alltheplanetfivetimes');
        var iv = CryptoJS.enc.Base64.parse('doesnotmeanindividualvaluebutgardens7890102345blueworld');

        if(file) {
        var reader = new FileReader();
        reader.readAsText(file, "utf-8");

        reader.onload = function(evt) {
        var decrypted = CryptoJS.AES.decrypt(evt.target.result, password, key, {mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7});
         $('#text').val(""+decrypted.toString(CryptoJS.enc.Utf8));
         decrypted.name = file.name;
         $('#name').val(decrypted.name);
        }

        }

        };