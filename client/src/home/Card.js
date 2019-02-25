import React from 'react';
import HomeMediaCard from '../home/HomeMediaCard.js';
import FeaturedCard from './FeaturedCard'
import styled from 'styled-components';

const CardTitle = styled.h1`
    font-family: 'Nirmala UI', sans-serif;
    font-weight: 800;
    font-size: 0.8em;
    color: #6A6A6A;
`;

const CardDetails = styled.h1`
    font-family: 'Nirmala UI', sans-serif;
    font-size: 0.8em;
    color: #6A6A6A;
`;

const ProfileCardTitle = CardTitle.extend`
    text-align: center;
`;

const EventCard = (props) => (
    <HomeMediaCard imgSrc={props.item.poster_url} imgAlt={props.item.photo_alt}>
        <CardTitle>{props.item.name}</CardTitle>
        <CardDetails>
            <p>{props.item.event_logistics[0].date};
                {props.item.event_logistics[0].start_time}-{props.item.event_logistics[0].end_time}</p>
            <p>{props.item.event_logistics[0].venue}</p>
            <p>{props.item.all_hosts.join(', ')}</p>
        </CardDetails>
    </HomeMediaCard>
);

const ProfileCard = (props) => (
    <HomeMediaCard imgHeight="100px" imgSrc={props.item.logo_url} imgAlt={props.item.photo_alt} imgSize='188px'>
        <ProfileCardTitle>{props.item.name}</ProfileCardTitle>
    </HomeMediaCard>
);

const Card = (props) => {
    if(props.card_type === 'event'){
        return <EventCard item={props.item}/>;
    } else if (props.card_type === 'profile'){
        return <ProfileCard item={props.item}/>;
    } else if (props.card_type === 'featured'){
        return <FeaturedCard item={props.item}/>;
    } else {
        return <div>Failed to load events.</div>;
    }
}

export default Card;