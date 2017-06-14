# coding: utf-8
print 'Content-Type: text/html\r\n\r\n'
print
print '''
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.js"></script>
</head>
<body>
<input type="file" />
<div class="console" style="width: 100%;"></div>
<button onclick="send();">Send</button>
<script>
    function send(){
        var data;

        data = new FormData();
        data.append( 'file1', $('input').get(0).files[0] );
        data.append( 'file2[]', new Blob([0xb4, 0xfa, 0xb8, 0xd5]) );
        data.append( 'file2[]', new Blob([0xb4, 0xfa, 0xb8, 0xd5]) );
        data.append( 'file2[]', new Blob([0xb4, 0xfa, 0xb8, 0xd5]) );

        $.ajax({
            url: '/cgi-bin/recv.py',
            data: data,
            processData: false,
            type: 'POST',
            success: function ( data ) {
                // alert( data );
                $('.console').text(data);
            }
        });
    }
</script>
</body>
</html>
'''