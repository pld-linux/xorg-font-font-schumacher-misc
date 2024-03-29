Summary:	Schumacher Clean bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe Schumacher Clean
Name:		xorg-font-font-schumacher-misc
Version:	1.1.3
Release:	1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-schumacher-misc-%{version}.tar.xz
# Source0-md5:	660e0449cebc1296d28ce58174fe0a71
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Schumacher Clean bitmap fonts.

This package includes Unicode fonts as well as in ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5, ISO-8859-7,
ISO-8859-8, ISO-8859-9, ISO-8859-10, ISO-8859-13, ISO-8859-14,
ISO-8859-15, ISO-8859-16 and KOI8-R encodings.

%description -l pl.UTF-8
Fonty bitmapowe Schumacher Clean.

Ten pakiet zawiera fonty unikodowe, a także w kodowaniach ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5, ISO-8859-7,
ISO-8859-8, ISO-8859-9, ISO-8859-10, ISO-8859-13, ISO-8859-14,
ISO-8859-15, ISO-8859-16 i KOI8-R.

%prep
%setup -q -n font-schumacher-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/misc/cl*.pcf.gz
