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

(()=>{
    navToggle();
})()