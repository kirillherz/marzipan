var Validators = {};
Validators.int = function (value) {
    return isNaN(parseInt(value));
};
Validators.float = function (value) {
    return isNaN(parseFloat(value));
};

function showError(input) {
    var data_validator_id = input.getAttribute("data-validator-id");
    var element = document.querySelector("div[data-validator-id = '" + data_validator_id + "']");
    element.style.display = "block";
}
function resetError(input) {
    var data_validator_id = input.getAttribute("data-validator-id");
    var element = document.querySelector("div[data-validator-id = '" + data_validator_id + "']");
    element.style.display = "none";
}

document.addEventListener("DOMContentLoaded", function () {
    var forms = document.getElementsByTagName("form");
    for (var i = 0; i !== forms.length; i++) {
        forms[i].addEventListener("submit", function () {
            var inputs = this.querySelectorAll("input[data-validator]");
            for (var j = 0; j !== inputs.length; j++) {
                var data_validator_value = inputs[j].getAttribute("data-validator");
                if (data_validator_value in Validators) {
                    if (Validators[data_validator_value](inputs[j].value)) {
                        showError(inputs[j]);
                        event.preventDefault();
                    } else {
                        resetError(inputs[j]);
                    }
                }
            }
        });
    }
});