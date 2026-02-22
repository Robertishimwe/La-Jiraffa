document.addEventListener("DOMContentLoaded", function () {
	const headerPlaceholder = document.getElementById("la-jiraffa-header-placeholder");
	if (headerPlaceholder) {
		const isHome = document.body.classList.contains('home');
		const customStyles = !isHome ? `
			<style>
				body:not(.home) .transparent.top-bar,
				body:not(.home) .transparent.top-bar a:not(:hover),
				body:not(.home) .transparent.top-bar .anpstext-desc {
					color: #ffffff !important;
				}
				@media(min-width: 992px) {
					body:not(.home) .site-header-style-transparent:not(.site-header-sticky-active) .site-navigation ul:not(.sub-menu)>li>a,
					body:not(.home) .site-header-style-transparent:not(.site-header-sticky-active) .site-search-toggle button:not(:hover):not(:focus),
					body:not(.home) .site-header-style-transparent:not(.site-header-sticky-active) .nav-empty {
						color: #ffffff !important;
					}
					body:not(.home) .site-header.site-header-sticky-active .site-navigation .menu-item-depth-0>a:not(:hover):not(:focus) {
						color: #000000 !important;
					}
				}
			</style>
		` : "";
		headerPlaceholder.innerHTML = customStyles + `
			<div class="site-search" id="site-search">
				<div class="container">
					<form role="search" method="get" class="site-search-form" action="javascript:void(0)">
						<input name="s" type="text" class="site-search-input"
							placeholder="type and press 'enter'">
					</form>
					<button class="site-search-close">&times;</button>
				</div>
			</div>
			<div class="transparent top-bar">
				<div class="container">
					<div class="top-bar-left">
						<div class="widget-container widget_anpssocial">
							<ul class="social">
								<li>
									<a href="https://www.facebook.com/profile.php?id=100089223604650" target="_blank">
										<i class="fa fa-facebook" aria-hidden="true"></i>
										<span class="sr-only">Facebook</span>
									</a>
								</li>
								<li>
									<a href="https://x.com/la_jiraffa" target="_blank">
										<i class="fa-brands fa-x-twitter" aria-hidden="true"></i>
										<span class="sr-only">X</span>
									</a>
								</li>
								<li>
									<a href="https://www.linkedin.com/in/la-jiraffa-154a31377/" target="_blank">
										<i class="fa fa-linkedin" aria-hidden="true"></i>
										<span class="sr-only">LinkedIn</span>
									</a>
								</li>
								<li>
									<a href="https://www.instagram.com/la_jiraffa/" target="_blank">
										<i class="fa fa-instagram" aria-hidden="true"></i>
										<span class="sr-only">Instagram</span>
									</a>
								</li>
							</ul>
						</div>
					</div>
					<div class="top-bar-right">
						<div class="widget-container widget_anpstext">
							<div class="anpstext-wrap">
								<span class="anpstext-arrow"></span>
								<span class="fa fa-clock-o"></span>
								<div class="anpstext-desc">Mon - Sat: 7:00 - 17:00</div>
							</div>
						</div>
						<div class="widget-container widget_anpstext">
							<div class="anpstext-wrap">
								<span class="anpstext-arrow"></span>
								<span class="fa fa-phone"></span>
								<div class="anpstext-desc">+250783490762</div>
							</div>
						</div>
						<div class="widget-container widget_anpstext">
							<div class="anpstext-wrap">
								<span class="anpstext-arrow"></span>
								<span class="fa fa-envelope-o"></span>
								<div class="anpstext-desc"><a href="mailto:info@lajiraffa.rw">info@lajiraffa.rw</a>
								</div>
							</div>
						</div>
					</div>
				</div> <button class="top-bar-close">
					<i class="fa fa-chevron-down"></i>
					<span class="sr-only">Close top bar</span>
				</button>
			</div>
			<header
				class="site-header site-header-sticky site-header-layout-normal site-header-style-transparent site-header-dropdown-1">
				<div class="nav-wrap">
					<div class="container">
						<div class="site-logo"><a href="index.html"> <img style="height:80px;width:200px;"
									class="logo-sticky" alt="Site logo"
									src="./images/La Giraffa Logo - No bg (Black) short.png">
								<img style="height:80px;width:200px;" class="logo-mobile" alt="La Jiraffa"
									src="./images/La Giraffa Logo - No bg (Black) short.png">
								<img class="logo-desktop" style="width:200px;height:80px;filter:invert(1);"
									alt="Site logo" src="./images/La Giraffa Logo - No bg (Black) short.png">
							</a></div>
						<div class="nav-bar-wrapper">
							<div class="nav-bar">
								<nav class="site-navigation">
									<ul class="">
										<li
											class="menu-item menu-item-type-post_type menu-item-object-page menu-item-depth-0">
											<a href="index.html">Home</a>
										</li>
										<li
											class="menu-item menu-item-type-post_type menu-item-object-page menu-item-depth-0">
											<a href="index.html#projects">Projects</a>
										</li>
										<li
											class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-depth-0">
											<a href="index.html#services">What we do</a>
											<ul class="sub-menu">
												<li class="menu-item menu-item-depth-1">
													<a href="index.html#services">Construction</a>
												</li>
												<li class="menu-item menu-item-depth-1">
													<a href="index.html#services">Renovations</a>
												</li>
												<li class="menu-item menu-item-depth-1">
													<a href="index.html#services">Consulting</a>
												</li>
												<li class="menu-item menu-item-depth-1">
													<a href="index.html#services">Architecture</a>
												</li>
											</ul>
										</li>
										<li
											class="menu-item menu-item-type-post_type menu-item-object-page menu-item-depth-0">
											<a href="index.html#about">About us</a>
										</li>
										<li
											class="menu-item menu-item-type-post_type menu-item-object-page menu-item-depth-0">
											<a href="contact.html">Contact us</a>
										</li>
									</ul>
								</nav>
								<div class="site-search-toggle">
									<button class="fa fa-search"><span class="sr-only">Search</span></button>
								</div>
								<button class="navbar-toggle" type="button">
									<span class="sr-only">Toggle navigation</span>
									<i class="fa fa-bars" aria-hidden="true"></i>
								</button>
							</div>
						</div>
					</div>
				</div>
			</header>`;
	}
});
