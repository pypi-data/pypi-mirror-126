const DEFAULT_TITLE = "ppt-control";
const LABEL_STOPPED = "Slideshow stopped";
const LABEL_RUNNING = "Slideshow running";
const LABEL_DISCONNECTED = "Disconnected";
const LABEL_FINAL_PREFIX = "Final slide &#8208; ";
const LABEL_END_PREFIX = "End of slideshow &#8208; ";
var preloaded = false;
var preload = [];

var presentation = document.querySelector('#presentation'),
    startBtn = document.querySelector('.start'),
    stopBtn = document.querySelector('.stop'),
    prev = document.querySelector('#prev'),
    next = document.querySelector('#next'),
    first = document.querySelector('#first'),
    last = document.querySelector('#last'),
    black = document.querySelector('#black'),
    white = document.querySelector('#white'),
    slide_label = document.querySelector('#slide_label'),
    current = document.querySelector('#current'),
    total = document.querySelector('#total'),
    status_text = document.querySelector('.status_text'),
    presentation_text = document.querySelector('.presentation_text'),
    current_img = document.querySelector('#current_img'),
    next_img = document.querySelector('#next_img'),
    current_div = document.querySelector('#current_div'),
    next_div = document.querySelector('#next_div'),
    controls_container = document.querySelector('#controls_container'),
    controls_container_inner = document.querySelector('#controls_container_inner'),
    show_current = document.querySelector('#show_current'),
    show_next = document.querySelector('#show_next'),
    shortcuts = document.querySelector('#shortcuts');

var presentationData = {};
var presentationOptions = {};


function getPresentationName() {
    if (presentation.selectedOptions.length > 0) {
        return presentation.selectedOptions[0].innerText;
    } else {
        return "";
    }
}


function startWebsocket() {
    console.log("Attempting to connect")
    ws = new WebSocket("ws://" + window.location.host + ":5678/");
    ws.onmessage = receive_message;
    ws.onclose = function(){
        ws = null;
        setTimeout(function(){websocket = startWebsocket()}, 1000);
    }
    if (ws.readyState !== WebSocket.OPEN) {
      disconnect()
    }
    return ws;
}

var websocket = startWebsocket();

prev.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'prev'}));
    }
}

next.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'next'}));
    }
}

first.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'first'}));
    }
}

last.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'last'}));
    }
}

black.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'black'}));
    }
}

white.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'white'}));
    }
}

current.onblur = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'goto', value: current.value}));
    }
}

startBtn.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'start'}));
    }
}

stopBtn.onclick = function (event) {
    if (getPresentationName()) {
        websocket.send(JSON.stringify({presentation: getPresentationName(), action: 'stop'}));
    }
}

current.addEventListener('keyup',function(e){
    if (e.which == 13) this.blur();
});


presentation.addEventListener('change',function(event){
    refreshInterface();
});

current_img.onclick = function (event) {
	next.click()
}

next_img.onclick = function (event) {
	next.click()
}

window.addEventListener('resize', function(event) {set_control_width()}, true);


function sync_current() {
    if (show_current.checked) {
        current_div.style.display = "block";
        slide_label.style.display = "none";
        next_div.style.width = "25%";
    } else {
        current_div.style.display = "none";
        slide_label.style.display = "inline";
        next_div.style.width = "calc(100% - 20px)";
    }
    set_control_width();
    saveSettings();
}
show_current.onclick = sync_current;

function sync_next() {
    if (show_next.checked) {
        next_div.style.display = "block";
        current_div.style.width = "70%";
    } else {
        next_div.style.display = "none";
        current_div.style.width = "calc(100% - 20px)";
    }
    set_control_width();
    saveSettings();
}
show_next.onclick = sync_next;

function sync_shortcuts() {
  saveSettings();
}
shortcuts.onclick = sync_shortcuts;

function set_control_width() {
	var width = window.innerWidth
	|| document.documentElement.clientWidth
	|| document.body.clientWidth;
    if (show_current.checked && show_next.checked && width > 800) {
        controls_container_inner.style.width = "70%"
    } else {
    	controls_container_inner.style.width = "100%"
    }
}


document.addEventListener('keydown', function (e) {
	if (shortcuts.checked) {
		switch (e.key) {
			case "Left":
			case "ArrowLeft":
			case "Up":
			case "ArrowUp":
			case "k":
			case "K":
				prev.click();
				break;
			case " ":
			case "Spacebar":
			case "Enter":
			case "Right":
			case "ArrowRight":
			case "Down":
			case "ArrowDown":
			case "j":
			case "J":
				next.click();
				break;
			case "b":
			case "B":
				black.click();
                break;
			case "w":
			case "W":
				white.click();
			default:
				return
		}
	}
});

function refreshInterface() {
    var d = new Date;
    if (Object.keys(presentationData).length > 0) {
        currentPresentationData = presentationData[getPresentationName()];
        presentation_text.style.display = "block";
        status_text.innerHTML = LABEL_RUNNING;
        startBtn.style.display = "none";
        stopBtn.style.display = "block";
        if (show_current.checked) {
            switch (currentPresentationData.visible) {
                case 3:
                    current_img.src = "/black.jpg";
                    break;
                case 4:
                    current_img.src = "/white.jpg";
                    break;
                default:
                    current_img.src = "/cache/" + currentPresentationData.name + "/" + currentPresentationData.slide_current + ".jpg?t=" + d.getTime();
                    break;
            }
        }
        if (currentPresentationData.slide_current == currentPresentationData.slide_total) {
            status_text.innerHTML = LABEL_FINAL_PREFIX + LABEL_RUNNING;
        }
        if (currentPresentationData.slide_current == currentPresentationData.slide_total + 1) { 
            status_text.innerHTML = LABEL_END_PREFIX + LABEL_RUNNING;
            next_img.src = "/black.jpg";
        } else {
            next_img.src = "/cache/" + currentPresentationData.name + "/" + (currentPresentationData.slide_current + 1) + ".jpg?t=" + d.getTime();
        }
        if (currentPresentationData.slide_current == 0) {
            current_img.src = "/black.jpg";
            next_img.src = "/black.jpg";
            status_text.innerHTML = LABEL_STOPPED;
            startBtn.style.display = "block";
            stopBtn.style.display = "none";
        }

        if (document.activeElement != current) {
            current.value = currentPresentationData.slide_current;
        }
        total.textContent = currentPresentationData.slide_total;
        document.title = currentPresentationData.name;
    } else {
        disconnect()
    }
}

function disconnect() {
    console.log("Disconnecting")
    document.title = DEFAULT_TITLE;
    current_img.src = "/black.jpg";
    next_img.src = "/black.jpg";
    status_text.innerHTML = LABEL_DISCONNECTED;
    total.textContent = "?";
    current.value = "";
    presentation_text.style.display = "none";
    startBtn.style.display = "none";
    stopBtn.style.display = "none";
}

function receive_message(event) {
    data = JSON.parse(event.data);
    if (Object.keys(presentationData).includes(data.name)) {
        // Existing presentation
        presentationData[data.name] = {"name": data.name, "pres_open": data.pres_open, "slideshow": data.slideshow, "visible": data.visible, "slide_current": data.slide_current, "slide_total": data.slide_total, "option": presentationData[data.name].option};
    } else {
        console.log("Adding new presentation " + data.name);
        var dropdownOption = document.createElement("option");
        dropdownOption.textContent = data.name;
        dropdownOption.value = data.name;
        presentationData[data.name] = {"name": data.name, "pres_open": data.pres_open, "slideshow": data.slideshow, "visible": data.visible, "slide_current": data.slide_current, "slide_total": data.slide_total, "option": dropdownOption};
        presentation.appendChild(dropdownOption);
    }
    if (! presentationData[data.name].pres_open) {
        presentation.removeChild(presentationData[data.name].option);
        delete presentationData[data.name]
        disconnect()
        
        //console.log("Deleting presentation data from list");
        //delete presentationData[data.name];
        //presentationOptions[data.name].remove()
    }
    refreshInterface()
        
	if (preloaded == false && ! isNaN(total.textContent)) {
		image = document.getElementById("preload_img");
		for (let i=1; i<=Number(total.textContent); i++) {
			image.src = "/cache/" + getPresentationName() + "/" + i + ".jpg";
			preload.push(image);
		}
		preloaded = true;
	}

};
