% This document class provides a simple memo for LaTeX users.
% It is based on article.cls and inherits most of the functionality
% that class.
% 
% Author: Rob Oakes, Copyright 2010.  Released under the LGPL, version 3.
% A copy of the LGPL can be found at http://www.gnu.org/licenses/lgpl.html

% Modified:  Eric Gibbons, Weber State University Department of Electrical
% and Computer Engineering.  

% Modified again: Ty Davis, Webet State University Department of Electrical
% and Computer Engineering STUDENT.

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{report}[2010/07/31 - Simple Memo Class, Including Logo]
%\RequirePackage{palatino}

% Load the Base Class
\LoadClassWithOptions{article}

% Begin Requirements
\RequirePackage{ifthen}
\RequirePackage{enumitem}

% Specialized memo Commands (To, From, Subject, Logo, Letterhead Address)

\def\@memostudent{\relax}
\newcommand{\memostudent}[1]{\gdef\@memostudent{#1}}

\def\@memocourse{\relax}
\newcommand{\memocourse}[1]{\gdef\@memocourse{#1}}

\def\@memotitle{\relax}
\newcommand{\memotitle}[1]{\gdef\@memotitle{#1}}

\def\@memodate{\relax}
\newcommand{\memodate}[1]{\gdef\@memodate{#1}}


\def\@letterheadaddress{\relax}
\newcommand{\lhaddress}[1]{\gdef\@letterheadaddress{#1}}

% Custom Document Formatting
\newcommand\decorativeline[1][1pt]{
	\par\noindent%
	\rule[0.5ex]{\linewidth}{#1}\par
}

% Set the Paper Size and margins
\RequirePackage{geometry}
\geometry{top=1.0in,left=0.75in,right=0.75in,bottom=0.75in}
\RequirePackage[parfill]{parskip} % no indent on paragraphs

% Useful imports for all of the lab reports
\RequirePackage{graphicx}
\RequirePackage{siunitx}
\RequirePackage{hyperref}
\RequirePackage[section]{placeins}
\RequirePackage{booktabs}


% Create the Letterhead and To/From Block

\renewcommand{\maketitle}{\makememotitle}
\newcommand\makememotitle{
	% To, From, Subject Block
	\begin{description}[itemsep=-0.7mm]
		\ifthenelse{\equal{\@memotitle}{\relax}}{}{\item [{}] {\large\textbf\@memotitle}}
		\ifthenelse{\equal{\@memostudent}{\relax}}{}{\item \@memostudent}
		\ifthenelse{\equal{\@memocourse}{\relax}}{}{\item [\relax] \@memocourse}
		\ifthenelse{\equal{\@memodate}{\relax}}{}{\item \@memodate}
	\end{description}
	\decorativeline\bigskip{}
}
