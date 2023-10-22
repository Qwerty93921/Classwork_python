let visitors = [
    { id: 1, name: "Collette Kelley", phone: "012 435 45 67" },
    { id: 2, name: "Ruby-rose Lennon", phone: "012 647 34 24" },
    { id: 3, name: "Rumaisa Peel", phone: "012 879 78 45" },
    { id: 4, name: "Gene Medrano", phone: "012 456 64 67" },
    { id: 5, name: "Sheddan Tucker", phone: "012 245 47 89" },
    { id: 6, name: "Christina Mack", phone: "012 345 85 90" },
    { id: 7, name: "Everly Moses", phone: "012 123 36 46" },
    { id: 8, name: "Kara Feeney", phone: "012 678 99 74" },
    { id: 9, name: "Cameron Rennie", phone: "012 456 96 53" },
    { id: 10, name: "Leanne Gibbons", phone: "012 967 47 85" },
  ];

function addVisitor() {

    const name = prompt("Введите имя посетителя:");
    const phone = prompt("Введите номер телефона:");

    const id = visitors.length + 1;

    const newVisitor = { id, name, phone };
    visitors.push(newVisitor);

    updateTable();
  }

  function editVisitor(id) {
    const visitor = visitors.find(v => v.id === id);
    if (visitor) {
      const newName = prompt("Введите новое имя:", visitor.name);
      const newPhone = prompt("Введите новый номер телефона:", visitor.phone);

      visitor.name = newName;
      visitor.phone = newPhone;

      updateTable();
    }
  }

  function updateTable() {
    const tableBody = document.querySelector("tbody");
    tableBody.innerHTML = "";

    for (const visitor of visitors) {
      const row = document.createElement("tr");
      row.innerHTML = `
        <th class="border-short" scope="row">${visitor.id}</th>
        <td class="border-long">${visitor.name}</td>
        <td class="border-long">${visitor.phone}</td>
        <td class="border-short">
          <button style="border: none;" onclick="editVisitor(${visitor.id});">
            <img class="image-class" src="img/pen.png">
          </button>
        </td>
      `;

      tableBody.appendChild(row);
    }
  }

  window.onload = updateTable;

//   const addVisitorButton = document.getElementById("addVisitorButton");
//   addVisitorButton.addEventListener("click", addVisitor);
