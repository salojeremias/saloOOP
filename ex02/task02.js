<html>
<head>
    <title>Contains Number Checker</title>
    <script>
        var containsNumber = function(numbers, aNumber) {
            return numbers.includes(aNumbers);
        };

        function checkContainsNumber() {
            var numbers = [6,4,2,5,9,7,5,7,2];
            var numberToCheck = parseInt(document.getElementById("numberInput"))
            var resultDiv = document.getElementById("result")

            if (containsNumber(numbers, numberToCheck)) {
                resultDiv.textContent = "Array contains the number" + numberToCheck;
            }
        }
    </script>
</head>
<body>
    <label for="numberInput">Enter a number to check:</label>
    <input type="text" id="numberInput"></input>
    <button onclick="checkContainsNumber()">Check</button>
    <div id="result"></div>
</body>
</html>