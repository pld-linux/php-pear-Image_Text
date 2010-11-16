%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Image_Text
Summary:	%{_pearname} - comfortable processing of texts in images
Summary(pl.UTF-8):	%{_pearname} - komfortowe przetwarzanie tekstu w obrazkach
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c62ba5d96331a6ee9fc6b4babea574b9
Patch0:		fontpath.patch
URL:		http://pear.php.net/package/Image_Text/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-gd
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

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa pozwala na dodanie tekstu do dynamicznie generowanych
obrazków w sposób bardziej komfortowy niż dotychczas. Możliwe jest
przetwarzanie tekstów wielolinijkowych i manipulowanie:
- obramowaniem
- cieniem
- ustawieniem. Inną ciekawą cechą jest pozwolenie klasie na zmierzenie
  tekstu w zależności od rozmiaru czcionki i dzielenie go na linie, aby
  zmieścił się w podanym polu tekstowym.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

mv docs/%{_pearname}/example examples

# tests -> tests/%{_pearname}
install -d ./%{php_pear_dir}/tests/.tmp
mv ./%{php_pear_dir}/tests/{*,.tmp}
mv ./%{php_pear_dir}/tests/{.tmp,%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# tests should not be packaged
%{__rm} -r $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/*.php
%{_examplesdir}/%{name}-%{version}
