interface HealthResponse {
    uptime: number;
    message: string;
    date: Date;
}

export default class HealthController {
    public async getMessage(): Promise<HealthResponse> {
        return {
            uptime: process.uptime(),
            message: "Ok",
            date: new Date()
        };
    }
}