import { Get, Route, Controller } from "tsoa";

interface HealthResponse {
    uptime: number;
    message: string;
    date: Date;
}

@Route("/health")
class HealthController extends Controller {
    @Get("")
    public async getMessage(): Promise<HealthResponse> {
        return {
            uptime: process.uptime(),
            message: "Ok",
            date: new Date()
        };
    }
}

export default HealthController;