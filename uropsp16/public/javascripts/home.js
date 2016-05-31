// Container to hold other users' usernames if they are generated as a potential match by the server-side code.

$(document).ready(function() {
	//AJAX STUFF WHOOO
    $('#displaytext').hide();
	$('#pev-button-id').click(function (e){
		e.preventDefault();
		var field = $('#pev-field').val();
		console.log(field);
		$.ajax({
			data: {field},
			url: '/beginsim',
      		type: 'POST',
      		success: function(data) {
				console.log('Moment starting');
                $('#displaytext').text(data);
                $('#displaytext').show();
				},
			error: function(xhr, status, error) {
        		console.log("Uh oh there was an error: " + error);
      			}
    	});
	});

});

// (function swing() {
//      var ang  = 4,
//         dAng = 1,
//         dir  = 1,
//         box = document.getElementById("jarimage");
//     (function setAng(ang){
//         console.log("function entered");
//         box.style.webkitTransform =  'rotate('+ang+'deg)';
//         dir = -dir;
//         if (Math.abs(ang) > 0)
//             setTimeout(setAng, 100000, dir * (Math.abs(ang)-dAng));
//     })(ang);
// })();
// $(".button").on('click', function() {

// (function() {
//     var x, y, $elie, pos, nowX, nowY, i, $that, vel, deg, fade, curve, ko, mo, oo, grow, len;
    
//     // Returns a random integer between min and max  
//     // Using Math.round() will give you a non-uniform distribution!  
//     function ran(min, max)  
//     {  
//         return Math.floor(Math.random() * (max - min + 1)) + min;  
//     } 
    
//     function moveIt()
//     {
//         $("div.spec").each(function(i, v) {
//             $elie = $(v);
//             if (! $elie.data("time"))
//             {
//                 $elie.data("time", ran(30, 100));
//                 $elie.data("deg", ran(-179, 180));
//                 $elie.data("vel", ran(3, 10));  
//                 $elie.data("curve", ran(0, 1));
//                 $elie.data("fade", ran(0, 1));
                           
//             }
            
//             vel = $elie.data("vel");
//             deg = $elie.data("deg");
//             fade = $elie.data("fade");            
//             curve = $elie.data("curve");
//             grow = $elie.data("grow");
            
//             len = $elie.width();
//             if (grow > 0)
//                 len = Math.min(len + grow, 50);
//             else
//                 len = Math.max(len + grow, 20);
            
//             $elie.css("-moz-border-radius", len/2);
//             $elie.css("border-radius", len/2);
            
//             $elie.css("width", len);
//             $elie.css("height", len);
            
//             pos = $elie.position();            
            
//             $elie.data("time", $elie.data("time") - 1);
            
//             if (curve)
//                 $elie.data("deg", (deg + 5) % 180);
//             else
//                 $elie.data("deg", (deg - 5) % 180);
            
//             ko = $elie.css("-khtml-opacity");
//             mo = $elie.css("-moz-opacity");
//             oo = $elie.css("opacity");
//             if (fade)
//             {
//                 $elie.css("-khtml-opacity", Math.max(ko - .1, .5));
//                 $elie.css("-moz-opacity", Math.max(mo - .1, .5));
//                 $elie.css("opacity", Math.max(oo - .1, .5));
//             } else
//             {
//                 $elie.css("-khtml-opacity", Math.min(ko - -.1, 1));
//                 $elie.css("-moz-opacity", Math.min(mo - -.1, 1));
//                 $elie.css("opacity", Math.min(oo - -.1, 1));                
//             }
            
//             if (vel < 3)
//                 $elie.data("time", 0);
//             else
//                 $elie.data("vel", vel - .2);            
            
            
//             nowX = pos.left;
//             nowY = pos.top;

//             x = vel * Math.cos(deg * Math.PI/180);
//             y = vel * Math.sin(deg * Math.PI/180);
            
//             nowX = nowX + x;            
//             nowY = nowY + y;

//           	var w = (window.innerWidth);
//         	var h = (window.innerHeight);
            
//             if (nowX < 0)
//                 nowX = w + nowX;
//             else 
//                 nowX = (nowX % w);
            
//             if (nowY < 0)
//                 nowY = h + nowY;
//             else
//                 nowY = (nowY % h) ;            
//             $elie.css("left", nowX);
//             $elie.css("top",  nowY);
//         });
//     }
//     $(function() {
//         $(document.createElement('div')).appendTo('body').attr('id', 'box');
//         $elie = $("<div/>").attr("class","spec");
//         // Note that math random is inclussive for 0 and exclussive for Max
//         var w = (window.innerWidth);
//         var h = (window.innerHeight);
//         var density1 = 10/(490*490);
//         var totalspec = (w*h)*density1;

//         for (i = 0; i < totalspec; ++i)
//         {
//             $that = $elie.clone();  
//             $that.css("top", ran(0, h));
//             $that.css("left", ran(0, w));            
//             $("#box").append($that);            
//         }          
//         timer = setInterval(moveIt, 60);
//         $("#sbox1").toggle(function() {
//             clearInterval(timer);
//             this.value = " Start ";
//         }, function() {
//             timer = setInterval(moveIt, 60);        
//             this.value = " Stop ";            
//         });        
//     });
// }());



//AJAX WORK PLS

		// $.ajax({
		// 	type: 'POST',
		// 	data: {},
		// 	url: '/createMatch',
		// 	dataType: 'JSON'
		// }).done(function(response) {
		// 	console.log('response');
		// });
// $.ajax({
// 			data: {'moment_jar':current_jar,'jarcontent':field},
// 			url: '/addmoment',
//       		type: 'POST',
//       		dataType: 'JSON',
//       		success: function(data) {
// 				$('#success').show();
// 				console.log('Moment starting');
// 				},
// 			error: function(xhr, status, error) {
//         		console.log("Uh oh there was an error: " + error);
//       			}

//     	});

		// $.ajax({
		// 	type: 'POST',
		// 	data: {'moment_jar':current_jar,'jarcontent':field},
		// 	url: '/addmoment',
		// 	dataType: 'JSON'
		// }).done(function(response){
		// 	// if(response.status = 
		// 	$('#success').show();
		// 	console.log('Moment starting');
		// })
 // $.ajax({
 //      url: '/adduser',
 //      data: {
 //        username: name,
 //        userfruit: fruit
 //      },
 //      type: 'POST',
 //      success: function(data) {
 //        // add a new list element containing the returned data
 //        $(".user-add").append("<li>" + data + "</li>");
 //      },
 //      error: function(xhr, status, error) {
 //        console.log("Uh oh there was an error: " + error);
 //      }
 //    });

// $('body').on('click','#addmoment',function(){
// 		$.ajax({
// 			type: 'POST',
// 			data: {'moment_jar':current_jar,'jarcontent':},
// 			url: '/addmoment',
// 			dataType: 'JSON'
// 		}).done(function(response){
// 			$('#success').show();
// 			console.log('Moment starting');
// 		})
// 	});
	// $('#addmoment').click(function(){
	// 	$.ajax({
	// 		type: 'POST',
	// 		data: {},
	// 		url: '/createMatch',
	// 		dataType: 'JSON'
	// 	}).done(function(response) {
	// 		// Check for successful response, show correct divs if response successful.
	// 		// On successful response, the potentialMatches array updates to hold this other user.
	// 		// Display the other user's username and the options to accept the match or try again.
	// 		if(response.status === 200) {
	// 			console.log('Successfully found a match, populating fields...');
	// 			$('#match-container').show();
	// 			potentialMatches = response.user;
	// 			$('#match-username').text(response.user.username);
	// 			$('#get-match').text('No, get me another match!');
	// 		} else {
	// 			if(response.status === 202) {
	// 				$('#message').text(response.msg);
	// 				$('#get-match').hide();
	// 				$('#redirect').show();
	// 			} else {
	// 				// If the call is not succesful, then print the error it ran into.
	// 				console.log('Error: ' + response.msg);
	// 			}
	// 		}
	// 	});
	// });

	// User agrees to potential match.
	// Send .ajax() post request to save the request.
	// $('#match-yes').click(function() {
	// 	$.ajax({
	// 		type: 'POST',
	// 		data: { 'recipient': potentialMatches.userId },
	// 		url: '/saveMatch',
	// 		dataType: 'JSON'
	// 	}).done(function(response) {
	// 		// On successful response, redirect to pending where the user can view their new match.
	// 		if(response === 200) {
	// 			console.log('Successfully saved match, redirecting to pending matches...');
	// 			window.location.replace('/pending');
	// 		} else {
	// 			console.log('Error: ' + response.msg);
	// 		}
	// 	});
	// });

// 	// Redirect to pending page
// 	$('#redirect').click(function(){
// 		window.location.replace('/pending');
// 	});
// });