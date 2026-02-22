// Reusable Footer Component
document.addEventListener("DOMContentLoaded", function () {
	const footerPlaceholder = document.getElementById("la-jiraffa-footer-placeholder");
	if (footerPlaceholder) {
		footerPlaceholder.innerHTML = `<footer class="site-footer style-1">
			<div class="container">
				<div class="row">
					<div class="col-md-3 col-xs-12">
						<div class="widget-container widget_anpsimages">
							<h3 class="widget-title">About us</h3>

							<!-- <img alt="La Jiraffa Logo" src="./images/La Giraffa Logo - No bg (Black) short.png" style="width:200px;height:200px;object-fit:contain;filter:invert(1)"/> -->
							<!-- <img alt="La Jiraffa Logo" src="./images/La Giraffa Logo - No bg (Black) short.png"
								style="width:200px;height:200px;object-fit:contain;filter:invert(1);display:block;margin:0;padding:0;" /> -->
							<img alt="La Jiraffa Logo" src="./images/La Giraffa Logo - No bg (Black) short.png"
								style="width:200px;height:80px;filter:invert(1);display:block;margin:0;padding:0;" />

						</div>
						<div id="text-4" class="widget-container widget_text" style="margin-top:0;">
							<div class="textwidget">
								<p>La Jiraffa specializes in construction and renovation projects in Rwanda, driven by a
									commitment to enhance the beauty of our world through exceptional and innovative
									designs.</p>
								<p><strong>Location:</strong> KK 44 Ave Kaleb building, Kigali, Rwanda</p>
							</div>
						</div>
					</div>
					<div class="col-md-3 col-xs-12">
						<div id="nav_menu-2" class="widget-container widget_nav_menu">
							<h3 class="widget-title">Navigation</h3>
							<div class="menu-main-menu-container">
								<ul id="menu-main-menu-1" class="menu">
									<li class="menu-item">
										<a href="index.html">Home</a>
									</li>
									<li class="menu-item">
										<a href="index.html#projects">Projects</a>
									</li>
									<li class="menu-item">
										<a href="index.html#services">What we do</a>
									</li>
									<li class="menu-item">
										<a href="index.html#about">About us</a>
									</li>
									<li class="menu-item">
										<a href="contact.html">Contact us</a>
									</li>
								</ul>
							</div>
						</div>
					</div>
					<div class="col-md-3 tablets-clear col-xs-12">
						<div id="tag_cloud-2" class="widget-container widget_tag_cloud">
							<h3 class="widget-title">Tags</h3>
							<div class="tagcloud"><a href="javascript:void(0)"
									class="tag-cloud-link tag-link-9 tag-link-position-1"
									style="font-size: 12pt;">big</a>
								<a href="javascript:void(0)" class="tag-cloud-link tag-link-10 tag-link-position-2"
									style="font-size: 12pt;">buildings</a>
								<a href="javascript:void(0)" class="tag-cloud-link tag-link-12 tag-link-position-3"
									style="font-size: 12pt;">home</a>
								<a href="javascript:void(0)" class="tag-cloud-link tag-link-13 tag-link-position-4"
									style="font-size: 12pt;">modern</a>
								<a href="javascript:void(0)" class="tag-cloud-link tag-link-14 tag-link-position-5"
									style="font-size: 12pt;">simple</a>
							</div>
						</div>
					</div>
					<div class="col-md-3 col-xs-12">
						<div id="anpsrecentprojects-2" class="widget-container anps-recent-posts">
							<h3 class="widget-title">Our recent projects</h3>
							<ul class="widget_recent_entries">

								<li>
									<a href="javascript:void(0)">Basil Construction</a>
								</li>



								<li>
									<a href="javascript:void(0)">JMV Karumuna</a>
								</li>



								<li>
									<a href="javascript:void(0)">Remera Project</a>
								</li>



								<li>
									<a href="javascript:void(0)">James Residence</a>
								</li>



								<li>
									<a href="javascript:void(0)">Gad Apartment</a>
								</li>

							</ul>
						</div>
					</div>
				</div>
			</div>
			<div class="copyright-footer">
				<div class="container">
					<div class="row">
						<div class="text-center">
							<div id="text-5" class="widget-container widget_text">
								<div class="textwidget">La Jiraffa | © 2025 La Jiraffa, All rights reserved</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</footer>`;
	}
});
