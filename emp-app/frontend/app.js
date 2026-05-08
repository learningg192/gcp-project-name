const API_URL = ""; // same server

function saveData() {
  const name = document.getElementById("name").value;
  const city = document.getElementById("city").value;

  fetch(`${API_URL}/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, city })
  })
    .then(res => {
      if (!res.ok) throw new Error("Failed to insert data");
      return res.json();
    })
    .then(() => {
      loadData();

      // clear input fields after insert
      document.getElementById("name").value = "";
      document.getElementById("city").value = "";
    })
    .catch(err => console.error("Error:", err));
}

function loadData() {
  fetch(`${API_URL}/get`)
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("result");
      list.innerHTML = "";

      data.forEach(row => {
        const li = document.createElement("li");
        li.innerText = `${row.name} - ${row.city}`;
        list.appendChild(li);
      });
    })
    .catch(err => console.error("Error:", err));
}

window.onload = loadData;