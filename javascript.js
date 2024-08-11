
        document.getElementById('menu-toggle').addEventListener('click', function() {
            document.getElementById('sidebar').classList.toggle('open');
            document.getElementById('content').classList.toggle('shifted');
        });

        document.getElementById('sidebar-close').addEventListener('click', function() {
            document.getElementById('sidebar').classList.remove('open');
            document.getElementById('content').classList.remove('shifted');
        });
