
const btn = document.querySelector('.calc-discount-btn');
const discountCodeInput = document.querySelector('.discount-code');

btn.addEventListener('click', () => {
  const table = document.querySelector('#ticket-table');
  const rows = table.querySelectorAll('tr');
  let total = 0;

  for(let i = 1; i < rows.length; i++) {
    const ticketCount = Number(rows[i].querySelectorAll('td')[7].textContent);
    const ticketCost = Number(rows[i].querySelectorAll('td')[3].textContent);
    total += ticketCount * ticketCost;
  }

  const discountCode = discountCodeInput.value;
  if(discountCode === 'SALE5%') {
    const discountTotal = (total * 0.95).toFixed(2);
    alert(`Total with your discount: ${discountTotal}`);
  } else {
    alert('Invalid discount code');
  }
});

