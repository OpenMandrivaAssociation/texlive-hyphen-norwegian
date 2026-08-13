%global tl_name hyphen-norwegian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Norwegian Bokmal and Nynorsk hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-norwegian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-norwegian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Norwegian Bokmal and Nynorsk in T1/EC and UTF-8
encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-norwegian:
bokmal loadhyph-nb.tex
=norwegian
=norsk
nynorsk loadhyph-nn.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-norwegian:
\addlanguage{bokmal}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{norwegian}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{norsk}{loadhyph-nb.tex}{}{2}{2}
\addlanguage{nynorsk}{loadhyph-nn.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-norwegian:
['bokmal'] = {
	loader = 'loadhyph-nb.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = { 'norwegian', 'norsk' },
	patterns = 'hyph-nb.pat.txt',
	hyphenation = 'hyph-nb.hyp.txt',
},
['nynorsk'] = {
	loader = 'loadhyph-nn.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-nn.pat.txt',
	hyphenation = 'hyph-nn.hyp.txt',
},
TL_HYPHEN_EOF
