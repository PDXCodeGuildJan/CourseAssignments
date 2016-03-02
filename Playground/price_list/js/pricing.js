// Establish the event listener for when they click an item
// Add the click event handler to the "add-item" button
var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

document.getElementById("del-item").addEventListener('click', deleteItem);

// Initialize the global variable that stores the inventory.
var products = [];

/* Toggles the inStock status on the selected
 * rows inside of inventory.
 */
function addStock() {
      // USE querySelectorAll()
   var selected = getSelectedRowBoxes();
   
   for (var i = 0; i < selected.length; i++) {
      var status = selected[i].parentNode.parentNode.children[3];
      status.textContent = "Yes";
      status.className = "true";

      // Update the Product in the products array that 
      // corresponds to the checked checkbox we're updating.
      var prodId = selected[i].parentNode.parentNode.id;
      products[prodId].inStock = true;

   };

}

function removeStock() {
   // USE querySelectorAll()
   var selected = getSelectedRowBoxes();
   
   for (var i = 0; i < selected.length; i++) {
      var status = selected[i].parentNode.parentNode.children[3];
      status.textContent = "No";
      status.className = "false";

      // Update the Product in the products array that 
      // corresponds to the checked checkbox we're updating.
      var prodId = selected[i].parentNode.parentNode.id;
      products[prodId].inStock = false;

   };

}

/* Add the item in the text fields to the inventory
 * list, which is in the table body (id="inventory")
 */
function addItem() {
   var materialName = document.getElementById("name").value;
   var price = document.getElementById("price").value;
   var inStock = document.getElementById("in-stock").checked;

   // Create a new instance of the Product 
   // object with the new Item's info
   var newProd = new Product(materialName, price, inStock);
   products.push(newProd);

   displayInventory();

}

/**
 * Delete the selected rows from the inventory.
 **/
function deleteItem() {

   // First, determine all the selected rows
   var selected = getSelectedRowBoxes();

   // Delete the Product objects that correspond
   // to those rows from the products array
   // Loop through the array backwards, so the 
   // indexes don't shift
   for (var i = selected.length-1; i >= 0; i--) {
      // Get the id on the row that the checkbox is in
      var prodId = parseInt(selected[i].parentNode.parentNode.id);

      // Delete the object first, leaving a gap
      delete products[prodId];
      // Then remove the gap in the list with a splice
      products.splice(prodId, 1);

   };

   // Rerender the HTML list, using displayInventory
   displayInventory();

}

/**
 * Helper function to get all the checked checkboxes in 
 * the HTML's inventory.
 * returns: array of selected checkboxes
 **/
function getSelectedRowBoxes() {
   var selected = document.querySelectorAll("tbody > tr > td > input:checked");
   return selected;
}

/**
 * Adds all the items in the products array to the HTML.
 **/
function displayInventory() {

   var inventory = document.getElementById("inventory");
   inventory.innerHTML = '';

   // Loop through the products array, adding each Product
   // to the inventory table in the html.
   for (var i = 0; i < products.length; i++) {
      // Make a new row for the Product i 
      var newRow = document.createElement("TR");
      newRow.id = i;

      // Make a TD for the checkbox
      var checkbox = document.createElement("TD");
      // Make the actual checkbox
      var innerCheckbox = document.createElement("INPUT");
      // Set the input type to checkbox
      innerCheckbox.type = "checkbox";
      // Add the checkbox into the TD
      checkbox.appendChild(innerCheckbox);

      // Make a TD for the material name
      var materialName = document.createElement("TD");
      materialName.textContent = products[i].prodName;

      // Make a TD for the price
      var price = document.createElement("TD");
      price.textContent = products[i].price;

      // Make a TD for the stock toggle
      var inStock = document.createElement("TD");
      // Set the TD's text content to either yes or no,
      // based on the product at index i's inStock property.
      inStock.textContent = (function(inStock) {
         if (inStock) {
            return "Yes";
         }
         return "No";
      }(products[i].inStock));
      // Set the class name on the td
      inStock.className = products[i].inStock;

      // Add all the TD's to the TR
      newRow.appendChild(checkbox);
      newRow.appendChild(materialName);
      newRow.appendChild(price);
      newRow.appendChild(inStock);

      // Add the new row to the actual TBODY in the HTML
      inventory.appendChild(newRow);

   };

   jsonProducts = JSON.stringify(products);
   console.log(jsonProducts);

}


/* Constructor for the Product object */
function Product(name, price, inStock) {
   this.prodName = name;
   this.price = price;
   this.inStock = inStock;

   this.setStock = function(stock) {
      this.inStock = stock;
   }
}
























