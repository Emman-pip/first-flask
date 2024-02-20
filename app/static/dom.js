const navToggle = () => {
  const burger = document.querySelector(".burger");
  const target = document.querySelector(".left");

  burger.addEventListener("click", (e) => {
    console.log("clicked")
    // target.style.transform = "translateX(10%)"
    target.classList.toggle("toView")
    // document.querySelector("body").style.backgroundColor = "white";
  });
};

const charts = () => {
    const ctx = document.getElementById('bdfar');
  
    new Chart(ctx, {
      type: 'bar',
      data: {
        // labels: {{ labels }},
        datasets: [{
          label: '# of Votes',
          // data: {{ data }},
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
}



(()=>{
  charts();
    navToggle();
})()