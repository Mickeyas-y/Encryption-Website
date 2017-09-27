  function encryptfile() {
        var file = document.getElementById("in_file").files[0];
        var password = $('#id_password').val();

        var key = CryptoJS.enc.Base64.parse('fly12345678alltheplanetfivetimes');
        var iv = CryptoJS.enc.Base64.parse('doesnotmeanindividualvaluebutgardens7890102345blueworld');

        if(file) {
        var reader = new FileReader();
        reader.readAsText(file, "utf-8");

        reader.onload = function(evt) {
        var encrypted = CryptoJS.AES.encrypt(evt.target.result, password, key, {iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7});
         $('#text').val(""+encrypted);
         encrypted.name = file.name;
         $('#name').val(encrypted.name);
        }

        }

        };

