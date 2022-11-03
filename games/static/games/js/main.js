    const popLinks = document.querySelectorAll('.popup_link');
    const body = document.querySelector('body');
    //console.log(body.style);
    const lockPadding = document.querySelectorAll('.lock-pad');
    let unlock = true;
    const timeout = 800;

    if (popLinks.length >0) {
        for (let index=0; index < popLinks.length; index++) {
            const popLink = popLinks[index];
            popLink.addEventListener('click',function(e){
                const popName = popLink.getAttribute('href').replace('#','');
                const curentPop = document.getElementById(popName);
                popupOpen(curentPop);
                e.preventDefault();

            });
        }
    }

     const popCloseIcon = document.querySelectorAll('.close_p');
     if (popCloseIcon.length>0) {
        for (let index = 0;  index< popCloseIcon.length; index++) {
    const el = popCloseIcon[index];
    el.addEventListener('click', function(e){
        popupClose(el.closest('.popup'));
        e.preventDefault();
    });
        }
     }

     function popupOpen(curentPop) {
        if (curentPop&&unlock) {
            const popActive = document.querySelector('.popup.open');
            if (popActive) {
                popupClose(popActive, false);
            } else {
                bodyLock();
            }
            curentPop.classList.add('open');
            curentPop.addEventListener('click', function(e)
            {
                if (!e.target.closest('pop_content')) {
                    popupClose(e.target.closest('.popup'));
                }
            });
        }
     }

     function popupClose(popActive, doUnlock=true){
        if (unlock){
            popActive.classList.remove('open');
            if (doUnlock) {
                bodyUnlock();
            }
        }
     }

     function bodyLock(){
        const lockPadVal = window.innerWidth - document.querySelector('.wrapper').offsetWidth+'px';
        if (lockPadding.length>0){
            for (let i = 0; i < lockPadding.length; i++) {
                const el = lockPadding[i];
                el.style.paddingRight=lockPadVal;
            }
        }
        console.log(lockPadVal);
        body.style.paddingRight=lockPadVal;
        body.classList.add('lock');

        unlock=false;
        setTimeout(function(){
            unlock=true;
        }, timeout);
     }

     function bodyUnlock(){
        setTimeout(function(){
            if (lockPadding.length>0){
            for (let i = 0; i < lockPadding.length; i++) {
                const el = lockPadding[i];
                el.style.paddingRight='0px';
            }
        }
            body.style.paddingRight='0px';
            body.classList.remove('lock');
        }, timeout);

        unlock=false;
        setTimeout(function(){
            unlock=true;
        }, timeout);
     }

     document.addEventListener('keydown', function(e){
        if (e.which ==27){
            const popActive = document.querySelector('.popup.open');
            popupClose(popActive);
        }
     });