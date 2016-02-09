var Validators = {};
Validators.int = function (value) {
    var pattern = "^[0-9]+$";
    return value.match(pattern) !== null;
};
Validators.float = function (value) {
    var pattern = "^[0-9]+[.,]{1}[0-9]*$";
    return value.match(pattern) !== null;
};
Validators.e_mail = function (value) {
    var pattern = "^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$";
    return value.match(pattern) !== null;
};
Validators.url = function (value) {
    var pattern = "^((https?|ftp)\:\/\/)?([a-z0-9]{1})((\.[a-z0-9-])|([a-z0-9-]))*\.([a-z]{2,6})(\/?)$";
    return value.match(pattern) !== null;
};
Validators.required = function (value) {
    return value.trim().length > 0;
};

function apply_class() {
    var elements = document.querySelectorAll("[data-validator-id]");
    for (var i = 0; i != elements.length; i++) {
        var attribute = elements[i].getAttribute("data-class-reset");
        elements[i].setAttribute("class", attribute);
    }
}

function showError(input) {
    var data_validator_id = input.getAttribute("data-validator-id");
    var elements = document.querySelectorAll("[data-validator-id = '" + data_validator_id + "']");
    for (var i = 0; i != elements.length; i++) {
        var attribute = elements[i].getAttribute("data-class-error");
        if (attribute !== null) {
            elements[i].setAttribute("class", attribute);
        }
    }
}

function resetError(input) {
    var data_validator_id = input.getAttribute("data-validator-id");
    var elements = document.querySelectorAll("[data-validator-id = '" + data_validator_id + "']");
    for (var i = 0; i != elements.length; i++) {
        var attribute = elements[i].getAttribute("data-class-reset");
        if (attribute !== null) {
            elements[i].setAttribute("class", attribute);
        }
    }
}

function is_blank_validate(input) {
    var attribute = input.getAttribute("data-blank");
    if (attribute === "true" && input.value.trim().length === 0 && attribute !== null) {
        return true;
    } else {
        return false;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    apply_class();
    var forms = document.getElementsByTagName("form");
    for (var i = 0; i !== forms.length; i++) {
        forms[i].addEventListener("submit", function (event) {
            var inputs = this.querySelectorAll("[data-blank],[data-validator]");
            for (var j = 0; j !== inputs.length; j++) {
                var data_validator_value = inputs[j].getAttribute("data-validator");
                if (is_blank_validate(inputs[j])) {
                    resetError(inputs[j]);
                } else {
                    if (data_validator_value in Validators) {
                        if (Validators[data_validator_value](inputs[j].value)) {
                            resetError(inputs[j]);
                        } else {
                            showError(inputs[j]);
                            event.preventDefault();
                        }
                    }
                }
            }
        });
    }
});