/*!
* Start Bootstrap - Simple Sidebar v6.0.2 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    sidebarWrapper = document.body.querySelector('#sidebar-wrapper');
    contentWrapper = document.body.querySelector('#content-wrapper');
    toggle = document.querySelector('#sidebarToggle');

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }

        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            if (toggle.classList.contains('bi-arrow-bar-left')) {
                toggle.classList.replace('bi-arrow-bar-left', 'bi-arrow-bar-right');
            } else {
                toggle.classList.replace('bi-arrow-bar-right', 'bi-arrow-bar-left');
            }
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));   
        });
    };
});
