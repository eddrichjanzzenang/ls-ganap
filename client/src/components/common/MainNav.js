import React, { Component } from "react";
import styled from "styled-components";
import { Link } from "react-router-dom";

import homeIcon from "assets/icon-home.png";
import searchIcon from "assets/icon-search.png";
import logo from "assets/ls-ganap-logo.png";
import FullWidthContainer from "components/common/FullWidthContainer";
import PageContent from "components/common/PageContent";
import AuthButtonContainer from "containers/AuthButtonContainer";
import DashboardButtonContainer from "containers/DashboardButtonContainer";
import { media } from "style/style-utils";

const NavLink = ({ className, route, children }) => (
  <Link className={className} to={route}>
    {children}
  </Link>
);

const Image = ({ className, source, alt }) => (
  <img className={className} src={source} alt={alt} />
);

const Nav = FullWidthContainer.extend`
  position: fixed;
  top: 0;
  z-index: 999;
  width: 100%;
  height: ${props => props.theme.sizes.navHeight};
  background-color: #f9f9f9;
  font-family: "Quatro", sans-serif;
  text-transform: uppercase;

  ${media.mdScreen`
    border-top: solid 10px #C5A478;
  `}
`;

const NavList = styled.ul`
  display: grid;
  grid-template-columns: ${props => (props.isAuthenticated && props.userId ? "2fr 1fr 1fr 1fr 1fr;" : "2fr 1fr 1fr 1fr")};
  height: 100%;
  margin: 0;
  padding: 0;

  ${media.mdScreen`
    grid-template-columns: ${props => (
      props.isAuthenticated ? 
        props.userId != null ? "1fr 130px 130px 160px 130px" 
        : "1fr 150px 140px 130px"
          : "1fr 150px 140px 210px"
    )};
    width: 100%
  `}
`;

const NavListItem = styled.li`
  display: flex;
  align-items: center;
  justify-content: center;
  list-style: none;

  ${media.mdScreen`
    justify-content: flex-start;
  `}
`;

const Logo = styled(Image)`
  max-height: 2.4em;
`;

const Icon = styled(Image)`
  max-height: 25px;
`;

const MobileLink = styled(NavLink)`
  display: block;
  color: #e07b24;
  text-decoration: none;

  ${media.mdScreen`
    display: none;
  `}
`;

const DesktopLink = styled(NavLink)`
  display: none;
  color: #e07b24;
  text-decoration: none;

  ${media.mdScreen`
    display: block;
    width: 100%;
    text-align: right;
  `}
`;

const DesktopLogo = DesktopLink.extend`
  ${media.mdScreen`
    display:block;
    text-align: left;
  `}
`;

class MainNav extends Component {
  render() {
    return (
      <Nav>
        <PageContent>
          <NavList isAuthenticated={this.props.isAuthenticated} userId={this.props.userId}>
            <NavListItem>
              <MobileLink route="/">
                <Logo source={logo} alt="LS Ganap Logo" />
              </MobileLink>
              <DesktopLogo route="/">
                <Logo source={logo} alt="LS Ganap Logo" />
              </DesktopLogo>
            </NavListItem>
            <NavListItem>
              <MobileLink route="/">
                <Icon source={homeIcon} alt="Home Icon" />
              </MobileLink>
              <DesktopLink route="/">Home</DesktopLink>
            </NavListItem>
            <NavListItem>
              <MobileLink route="/browse">
                <Icon source={searchIcon} alt="Search Icon" />
              </MobileLink>
              <DesktopLink route="/browse">Browse</DesktopLink>
            </NavListItem>
            <DashboardButtonContainer />
            <NavListItem>
              <AuthButtonContainer />
            </NavListItem>
          </NavList>
        </PageContent>
      </Nav>
    );
  }
}

export default MainNav;
