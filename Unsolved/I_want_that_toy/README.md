# I want that toy
Pwn

## Challenge 

	Santa created a submission system that allows you to request toys for this Christmas. Give it a try!

	Server: http://199.247.6.180:10000/

	Libc: libc.so.6

	Author: littlewho

	server

## Solution

GET data

	Welcome to the X-MAS wishes API!

	Submit your desired toy by using ?toy parameter.
	For easier data handling, Santa wants your strings encoded in base64
	Example: GET /?parameter=base64_string 

	Be careful, Santa is logging your requests.
	I'm sure you don't want to be on the naughties' list. 
	[GET] / - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.116


POST data

	 $ curl --data "test" http://199.247.6.180:10000/
	Wow, seems that you POSTed 4 bytes. 
	Fetch the data using `payload` variable


	void route() {
	    if ((strcmp(0x1dbd, *uri) == 0x0) && (strcmp(0x1dbf, *method) == 0x0)) {
	            puts("HTTP/1.1 200 OK\r\n\r");
	            var_10 = request_query_var(0x1dd6);
	            printf("<html><head><title>X-MAS API</title><head><body style='background-color:#17272C; color:white;'>");
	            printf("<h1>Welcome to the <b>X-MAS</b> wishes API!</h1><br>");
	            if (var_10 == 0x0) {
	                    printf("Submit your desired toy by using ?toy parameter.<br>");
	                    printf("For easier data handling, Santa wants your strings encoded in base64<br>");
	                    printf("Example: <i>GET /?parameter=base64_string </i><br>");
	            }else {
	                    printf("Santa will bring you the <b>%s</b> this year!<br>", var_10);
	            }
	            puts("<br><br><br><br><footer><small> Be careful, Santa is logging your requests.<br> I'm sure you don't want to be on the naughties' list.");
	            printf("<br>[GET] %s - ", *uri);
	            printf(request_header("User-Agent"));
	            printf("</small></footer></body></html>");
	    }else {
	            if ((strcmp(0x1dbd, *uri) == 0x0) && (strcmp(0x2038, *method) == 0x0)) {
	                    puts("HTTP/1.1 200 OK\r\n\r");
	                    printf("Wow, seems that you POSTed %d bytes. \r\n", *(int32_t *)payload_size);
	                    printf("Fetch the data using `payload` variable.");
	            }
	            else {
	                    puts("HTTP/1.1 500 Not Handled\r\n\r\nThe server has no handler to the request.\r");
	            }
	    }
	}

## Flag

	??