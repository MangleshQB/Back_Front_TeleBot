<script>
    let cartItemsArray = [];

    function addToCart(name, price) {
      const item = cartItemsArray.find(item => item.name === name);

      if (item) {
        item.quantity++;
      } else {
        cartItemsArray.push({ name, price, quantity: 1 });
      }

      displayCartItems();
    }

    function removeFromCart(index) {
      cartItemsArray.splice(index, 1);
      displayCartItems();
    }

    function changeCartItemQuantity(index, change) {
      const item = cartItemsArray[index];
      const newQuantity = item.quantity + change;

      if (newQuantity >= 0) {
        item.quantity = newQuantity;
        displayCartItems();
      }
    }

    function displayCartItems() {
      const cartItemsElement = document.getElementById('cartItems');
      let cartItemsHtml = '';
      let totalPrice = 0;

      cartItemsArray.forEach((item, index) => {
        const itemTotal = item.price * item.quantity;
        totalPrice += itemTotal;
        cartItemsHtml += `
          <div class="d-flex justify-content-between align-items-center mb-2">
            <p>${item.name}: $${item.price.toFixed(2)} x ${item.quantity} = $${itemTotal.toFixed(2)}</p>
            <div>
              <button class="btn btn-sm btn-primary me-1" onclick="changeCartItemQuantity(${index}, -1)">-</button>
              <button class="btn btn-sm btn-primary me-1" onclick="changeCartItemQuantity(${index}, 1)">+</button>
              <button class="btn btn-sm btn-danger" onclick="removeFromCart(${index})">Remove</button>
            </div>
          </div>`;
      });

      document.getElementById('totalPrice').textContent = '$' + totalPrice.toFixed(2);
      cartItemsElement.innerHTML = cartItemsHtml;
    }
  </script>