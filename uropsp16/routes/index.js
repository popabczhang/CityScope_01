var express = require('express');
var router = express.Router();
var spawn = require("child_process").spawn;
var simul;
var finallist;
var path = require('path')


/* GET home page. */
router.get('/', function(req, res, next) {
	res.render('index');
});

router.post('/beginsim', function (req, res, next) {
	console.log("before");
	var pevback = req.body.field;
	console.log(pevback);
	simul = spawn('python',[path.join(__dirname, 'testing.py'), pevback]);
	console.log("after");
	simul.stdout.on('data', function (data){
		console.log(data.toString());
		res.send(data);
		});
});

module.exports = router;
