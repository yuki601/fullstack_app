import ClientPage from './ClientPage';

export default function Page({ params }: { params: { id: string } }) {
    return <ClientPage id={parseInt(params.id)} />;
}
