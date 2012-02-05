function toggleFilter(showHideDiv, switchImgTag) {
        var ele = document.getElementById(showHideDiv);
        var imageEle = document.getElementById(switchImgTag);
        if(ele.style.display == "block") {
                ele.style.display = "none";
		imageEle.innerHTML = '<img align=right src="/media/site_images/down_arrow.gif">';
        }
        else {
                ele.style.display = "block";
                imageEle.innerHTML = '<img align=right src="/media/site_images/up_arrow.gif">';
        }
}
