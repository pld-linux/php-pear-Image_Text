%define		status		beta
%define		pearname	Image_Text
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - comfortable processing of texts in images
Summary(pl.UTF-8):	%{pearname} - komfortowe przetwarzanie tekstu w obrazkach
Name:		php-pear-%{pearname}
Version:	0.7.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	034c356787c73dd1a88567bf01bb7923
Patch0:		fontpath.patch
URL:		http://pear.php.net/package/Image_Text/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= %{php_min_version}
Requires:	php(gd)
Requires:	php-pear
Obsoletes:	php-pear-Image_Text-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class allows you to add text to dynamic generated images more
comfortable. It allows you to process multiline text and manipulate:
- Border
- Shading
- Alignment Another nice feature is to let the class measurize your
  text in respect to font size and line splitting to fit a given text
  box.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ta klasa pozwala na dodanie tekstu do dynamicznie generowanych
obrazków w sposób bardziej komfortowy niż dotychczas. Możliwe jest
przetwarzanie tekstów wielolinijkowych i manipulowanie:
- obramowaniem
- cieniem
- ustawieniem. Inną ciekawą cechą jest pozwolenie klasie na zmierzenie
  tekstu w zależności od rozmiaru czcionki i dzielenie go na linie, aby
  zmieścił się w podanym polu tekstowym.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
%patch0 -p1

mv docs/%{pearname}/* .
mv .%{php_pear_dir}/tests/Image_Text/tests .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/Text.php
%{php_pear_dir}/Image/Text
%{_examplesdir}/%{name}-%{version}
