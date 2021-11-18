    document.getElementById("profile").style.display = "none"; 
    
    //variable to not overlap popups
    let x=false;


    //      LOGIN 

    document.querySelector("#login").addEventListener("click",function(){
        if(x==true)
        {
            document.querySelector(".popup1").classList.remove("active1");
        }
        document.querySelector(".popup").classList.add("active1");
        x=true;
    });

    document.querySelector(".popup .close-btn").addEventListener("click",function(){
        document.querySelector(".popup").classList.remove("active1");
        x=false;
    });

    document.querySelector("#signin").addEventListener("click",function()
    {
        document.querySelector(".popup").classList.remove("active1");
        document.getElementById("login").style.display = "none";
        document.getElementById("signup").style.display = "none";
        document.getElementById("profile").style.display = "block"; 
        x=false;
    });


    //              SIGNUP


    document.querySelector("#signup").addEventListener("click",function(){
        if(x==true)
        {
            document.querySelector(".popup").classList.remove("active1");
        }
        document.querySelector(".popup1").classList.add("active1");
        x=true;
    });
        

    document.querySelector(".popup1 .close-btn").addEventListener("click",function(){
        document.querySelector(".popup1").classList.remove("active1");
        x=false;
    });


    document.querySelector("#SignUp_Submit").addEventListener("click",function()
    {
        document.querySelector(".popup1").classList.remove("active1");
        document.getElementById("login").style.display = "none";
        document.getElementById("signup").style.display = "none";
        document.getElementById("profile").style.display = "block"; 
        x=false;
    });
    
