import React from "react";
import styled from "styled-components";

import AppButton from "components/common/AppButton";
import AppCardImage from "components/common/AppCardImage";
import AppHeading from "components/common/AppHeading";
import AppSubheading from "components/common/AppSubheading";
import AppText from "components/common/AppText";
import { media } from "style/style-utils";

const SlideArticle = styled.article`
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  ${media.mdScreen`
    flex-direction: row;
    align-items: center;
    height: 100%;
  `}
`;

const SlidePoster = styled(AppCardImage)`
  width: 35%;
`;

const TextBox = styled.div`
  width: 60%;
  height: 80%;
`;

const SlideHeadingH2 = AppHeading.withComponent("h2");
const SlideSubheadingP = AppSubheading.withComponent("p");
const SlideTextP = AppText.withComponent("p");

const SlideDescription = AppText.withComponent("p").extend`
  width: 75%;
  margin-bottom: 2rem;
`;

const FeaturedSectionSlide = ({
  name,
  formattedHosts,
  formattedDate,
  formattedTime,
  venue,
  poster_url,
  description
}) => (
  <SlideArticle>
    <SlidePoster src={poster_url} aspectRatio={4 / 3} />
    <TextBox>
      <SlideHeadingH2 size={4}>{name}</SlideHeadingH2>
      <SlideSubheadingP size={2} style={{ marginBottom: "1rem" }}>
        {formattedHosts}
      </SlideSubheadingP>
      <SlideTextP>{formattedDate}</SlideTextP>
      <SlideTextP>{formattedTime}</SlideTextP>
      <SlideTextP style={{ marginBottom: "1rem" }}>{venue}</SlideTextP>
      <SlideDescription>{description}</SlideDescription>
      <AppButton>Add to My Calendar</AppButton>
      <AppButton empty>Read More</AppButton>
    </TextBox>
  </SlideArticle>
);

export default FeaturedSectionSlide;