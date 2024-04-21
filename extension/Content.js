const generateSTYLES = () => {
  return `<style>@import url(https://fonts.googleapis.com/css?family=opensans:500);
      @keyframes sunrise {
        from {
          transform: rotate(-45deg);
        }
      
        to {
          transform: rotate(315deg);
        }
      }
      
      @keyframes moonrise {
        from {
          transform: rotate(0deg);
        }
      
        to {
          transform: rotate(180deg);
        }
      }
      
      @keyframes dawn {
        0% {
          opacity: 0;
        }
        10% {
          opacity: 1;
        }
        60% {
          opacity: 0;
        }
      }
      
      @keyframes noon {
        0% {
          opacity: 0;
        }
        50% {
          opacity: 1;
        }
        75% {
          opacity: 0;
        }
      }
      
      @keyframes dusk {
        0% {
          opacity: 0;
        }
        50% {
          opacity: 0;
        }
        70% {
          opacity: 1;
        }
        90% {
          opacity: 0;
        }
      }
      
      @keyframes midnight {
        0% {
          opacity: 1;
        }
        25% {
          opacity: 0;
        }
        50% {
          opacity: 0;
        }
        80% {
          opacity: 1;
        }
      }
      
      body {
        --animation-speed: 24s;
        background-color: rgb(37, 29, 24);
      }
      
      body.pause {
        --animation-speed: 0;
      }
      body{
        margin:0;
        padding:0;
        font-family: 'Tomorrow', sans-serif;
        height:100vh;
        display:flex;
        justify-content:center;
        align-items:center;
        overflow:hidden;}
      
      h1{
        font-size: 60px;
      }
      p{
        font-size: 40px;
      
      }
      .text{
        position: absolute;
        color: #FFF;
        top: 10%;
        text-align: center;
      }
      
      .sky {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        max-height: 600px;
        overflow: hidden;
      }
      
      .sky__phase {
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        transition: opacity 0.2s;
      }
      
      .sky__dawn {
        background: linear-gradient(
          0deg,
          rgba(254, 215, 102, 1) 0%,
          rgba(205, 237, 246, 1) 100%
        );
        animation: linear dawn infinite var(--animation-speed);
      }
      
      .sky__noon {
        background: linear-gradient(
          0deg,
          rgba(205, 237, 246, 1) 0%,
          rgba(36, 123, 160, 1) 100%
        );
        animation: linear noon infinite var(--animation-speed);
      }
      
      .sky__dusk {
        background: linear-gradient(
          0deg,
          rgba(255, 32, 110, 1) 0%,
          rgba(10, 0, 94, 1) 100%
        );
        animation: linear dusk infinite var(--animation-speed);
      }
      
      .sky__midnight {
        background: linear-gradient(
          0deg,
          rgba(2, 0, 20, 1) 0%,
          rgba(10, 0, 94, 1) 100%
        );
        animation: linear midnight infinite var(--animation-speed);
      }
      
      .orbit {
        position: relative;
        width: 500px;
        height: 500px;
        margin: 200px auto;
        transform: rotate(-45deg);
        animation: linear sunrise infinite var(--animation-speed);
      }
      
      @media (min-width: 768px) {
        .sky {
          max-height: 600px;
        }
        .orbit {
          width: 700px;
          height: 700px;
          margin: 150px auto;
        }
      }
      
      @media (min-width: 940px) {
        .orbit {
          width: 800px;
          height: 800px;
        }
      }
      
      @media (min-width: 1200px) {
        body {
          --animation-speed: 28s;
        }
        .orbit {
          width: 1000px;
          height: 1000px;
          margin: 200px auto;
        }
      }
      
      @media (min-width: 1500px) {
        body {
          --animation-speed: 30s;
        }
        .orbit {
          width: 1300px;
          height: 1300px;
        }
      }
      
      .sun {
        position: absolute;
        top: -40px;
        left: -40px;
        width: 80px;
        height: 80px;
        background-color: rgb(254, 215, 102);
        border-radius: 50%;
        box-shadow: 0 0 14px 14px rgba(254, 215, 102, 0.2);
      }
      
      .moon {
        position: absolute;
        bottom: -40px;
        right: -40px;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background-color: #fff;
        box-shadow: 0 0 7px 7px rgba(255, 255, 255, 0.2);
      }
      
      #sky__stars > div {
        width: 3px;
        height: 3px;
        background-color: #fff;
        border-radius: 50%;
        position: absolute;
      } 
   </style>`;
};

const generateHTML = () => {
  return `
   
      <head>
    <div class="text">
      <h1>ERROR</h1>
      <h1>404</h1>
      <p>Don't waste your time in this website >_<* </p>
      </div>
      <div class="sky">
      <div class="sky__phase sky__dawn"></div>
      <div class="sky__phase sky__noon"></div>
      <div class="sky__phase sky__dusk"></div>
      <div class="sky__phase sky__midnight">
        <div id="sky__stars"></div>
      </div>
      <div class="orbit">
        <div class="sun"></div>
        <div class="moon"></div>
      </div>
    </div>
    </head>
   `;
};
var list = [];
window.onload = function block(){
  /* REFERENCE:- https://www.youtube.com/watch?v=roYiXi-Eh8E&t=396s */
  const requestObj = new XMLHttpRequest()
  requestObj.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
          const string = this.responseText;
          list = string.trim().split(/\s+/); // blocked list
          console.log(list);
          var currWebsite = window.location.hostname; // current sites hostname
          for(var i=0; i<list.length; i++){
            if(list[i].includes(currWebsite)){
              /* block the site if the site is present in blocked list */
              document.head.innerHTML = generateSTYLES();
              document.body.innerHTML = generateHTML();
              console.log('Yes')
              break;
            }
        }
      }
  }
  requestObj.open("GET", 'http://127.0.0.1:8000/extension/get/') // get request to Django server
  requestObj.send()
}




/*
switch (window.location.hostname) {
  case "www.youtube.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("YOUTUBE");
    break;
  case "www.facebook.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("FACEBOOK");
    break;
  case "www.netflix.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("NETFLIX");
    break;
  case "www.roblox.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("ROBLOX");
    break;
  case "discord.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("DISCORD");
    break;
  case "www.spotify.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("SPOTIFY");
    break;
  case "www.instagram.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("INSTAGRAM");
    break;
  case "www.google.com":
    document.head.innerHTML = generateSTYLES();
    document.body.innerHTML = generateHTML("GOOGLE");
}

/*
window.onload = function block(){
  var sites=JSON.parse(localStorage.getItem('blocked'));
  console.log(sites);
  if(sites.length==0){
    console.log('Hello sophia! Hold up!');
  }
  console.log(window.location.hostname);
  for(var i=0; i<sites.length; i++){
    console.log(sites[i].innerHTML);
    if(sites[i]==window.location.hostname){
      document.head.innerHTML = generateSTYLES();
      document.body.innerHTML = generateHTML();
      break;
    }
  }
};
*/