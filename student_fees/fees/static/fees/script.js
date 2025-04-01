// // Dynamic behavior for the update fees form
// document.addEventListener("DOMContentLoaded", function() {
//     const form = document.querySelector('form');
//     const amountInput = document.querySelector('input[name="amount"]');

//     form.addEventListener('submit', function(event) {
//         const amount = parseFloat(amountInput.value);
//         if (isNaN(amount) || amount <= 0) {
//             alert("Please enter a valid amount.");
//             event.preventDefault();
//         } else {
//             alert("Fees updated successfully.");
//         }
//     });
// });

// // Optional: Add fee due calculation for analytics (if needed)
// function calculateFeeDue(totalFees, paidFees) {
//     const feeDue = totalFees - paidFees;
//     return feeDue;
// }

// // Example: Use calculateFeeDue function when needed in your project (dynamic data update).


// Search function for filtering students
function searchStudents() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let table = document.getElementById("studentTable");
    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        let name = rows[i].getElementsByTagName("td")[0].textContent.toLowerCase();
        let email = rows[i].getElementsByTagName("td")[1].textContent.toLowerCase();

        if (name.includes(input) || email.includes(input)) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}

// Sort function for table columns
function sortTable(n) {
    let table = document.getElementById("studentTable");
    let rows = Array.from(table.getElementsByTagName("tr")).slice(1);
    let switching = true;
    let direction = "asc";

    while (switching) {
        switching = false;
        for (let i = 0; i < rows.length - 1; i++) {
            let x = rows[i].getElementsByTagName("td")[n].textContent.toLowerCase();
            let y = rows[i + 1].getElementsByTagName("td")[n].textContent.toLowerCase();
            let shouldSwitch = false;

            if (direction === "asc" && x > y) {
                shouldSwitch = true;
            } else if (direction === "desc" && x < y) {
                shouldSwitch = true;
            }

            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }

        direction = (direction === "asc") ? "desc" : "asc";
    }
}
